from file_loader import load_filtered_content
from text_extractor import get_clear_text

urls = load_filtered_content('data/urls.txt')
get_clear_text(urls, 'data/extracted/clearText')
