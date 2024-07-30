# process_text.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dep_analysis.settings')
django.setup()

from analysis.utils import process_text_file

file_path = '1.txt'
process_text_file(file_path)
