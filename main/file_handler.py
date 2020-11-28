def load_filtered_content(file_name):
    f = open(file_name, 'r')
    urls = f.read().split()
    f.close()
    return list(dict.fromkeys(urls))


def clear_text(text, chars):
    for char in chars:
        text = text.replace(char, "")
    return text
