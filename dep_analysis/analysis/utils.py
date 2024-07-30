import spacy
from spacy import displacy
from .models import DependencyData, DependencyDataArticle
import os
from django.conf import settings
import re
import logging
from segtok import segmenter  # 确保正确导入segtok

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载spaCy模型
nlp = spacy.load("en_core_web_sm")


def split_multi_sents(text):
    return list(segmenter.split_multi(text))


def parse_and_save_sentences(sentences, is_article=False):
    for sentence in sentences:
        try:
            # 使用spaCy处理句子
            doc = nlp(sentence)

            # 生成有效的文件名
            valid_filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', sentence[:50])
            if is_article:
                image_path = os.path.join(settings.MEDIA_ROOT, 'media_article')
            else:
                image_path = settings.MEDIA_ROOT

            if not os.path.exists(image_path):
                os.makedirs(image_path)
                logger.info(f"Created directory: {image_path}")

            svg_path = os.path.join(image_path, f"{valid_filename}.svg")

            # 生成依存关系图并保存为SVG文件
            svg_content = displacy.render(doc, style="dep", jupyter=False)
            with open(svg_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
                logger.info(f"Saved SVG file: {svg_path}")

            # 提取对象数据和关系数据
            object_data = [{'text': token.text, 'dep': token.dep_} for token in doc]
            relation_data = [{'head_text': token.head.text, 'head_dep': token.head.dep_} for token in doc]

            if is_article:
                # 检查句子是否存在
                existing_record = DependencyDataArticle.objects.filter(sentence=sentence).first()
                if existing_record:
                    # 更新现有记录
                    existing_record.dep_svg_path = svg_path
                    existing_record.object_data = object_data
                    existing_record.relation_data = relation_data
                    existing_record.save()
                    logger.info(f"Updated DependencyDataArticle for sentence: {sentence[:50]}")
                else:
                    # 创建新记录
                    DependencyDataArticle.objects.create(
                        sentence=sentence,
                        dep_svg_path=svg_path,
                        object_data=object_data,
                        relation_data=relation_data
                    )
                    logger.info(f"Saved DependencyDataArticle for sentence: {sentence[:50]}")
            else:
                # 检查句子是否存在
                existing_record = DependencyData.objects.filter(sentence=sentence).first()
                if existing_record:
                    # 更新现有记录
                    existing_record.dep_svg_path = svg_path
                    existing_record.object_data = object_data
                    existing_record.relation_data = relation_data
                    existing_record.save()
                    logger.info(f"Updated DependencyData for sentence: {sentence[:50]}")
                else:
                    # 创建新记录
                    DependencyData.objects.create(
                        sentence=sentence,
                        dep_svg_path=svg_path,
                        object_data=object_data,
                        relation_data=relation_data
                    )
                    logger.info(f"Saved DependencyData for sentence: {sentence[:50]}")

        except Exception as e:
            logger.error(f"Error processing sentence: {sentence[:50]}")
            logger.error(str(e))


def process_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            logger.info(f"Read text file: {file_path}")

        sentences = split_multi_sents(text)
        logger.info(f"Split text into {len(sentences)} sentences")

        parse_and_save_sentences(sentences, is_article=True)

    except Exception as e:
        logger.error(f"Error processing file: {file_path}")
        logger.error(str(e))
