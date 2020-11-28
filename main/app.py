from file_handler import load_filtered_content
from text_extractor import get_clear_text

print("ŠČčšž...")
urls = load_filtered_content('data/urls.txt')
print("Clearing text...")
get_clear_text(urls, 'data/extracted/clearText')
