from django.db import models

class DependencyData(models.Model):
    sentence = models.TextField()
    dep_svg_path = models.CharField(max_length=255)
    object_data = models.JSONField(default=list)  # 添加默认值
    relation_data = models.JSONField(default=list)  # 添加默认值

    def __str__(self):
        return self.sentence

class DependencyDataArticle(models.Model):
    sentence = models.TextField()
    dep_svg_path = models.CharField(max_length=255)
    object_data = models.JSONField(default=list)  # 添加默认值
    relation_data = models.JSONField(default=list)  # 添加默认值

    def __str__(self):
        return self.sentence

class DependencyDataExamples(models.Model):
    sentence = models.TextField()
    dep_svg_path = models.CharField(max_length=255)
    object_data = models.JSONField(default=list)  # 添加默认值
    relation_data = models.JSONField(default=list)  # 添加默认值

    def __str__(self):
        return self.sentence
