# process_examples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dep_analysis.settings')
django.setup()

from analysis.utils import process_sentence_examples
from sentence_examples import sentence_examples

process_sentence_examples(sentence_examples)
