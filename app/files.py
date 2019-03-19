import os
import re


def file(files_name, mod, string_for_count=None, string_for_search=None, string_for_replace=None):
    BASE_DIR = os.path.join(os.getcwd(), files_name)
    if mod == 'c':
        try:
            with open(BASE_DIR, 'r') as file:
                text = file.read()
                return print(len(re.findall(f'(?={string_for_count})', text)))
        except FileNotFoundError:
            return print('File Not Found')
    elif mod == 'r':
        try:
            with open(BASE_DIR) as file:
                text = file.read()

            new_text = text.replace(string_for_search, string_for_replace)

            with open(BASE_DIR, 'w') as file:
                file.write(new_text)
        except FileNotFoundError:
            return print('File Not Found')