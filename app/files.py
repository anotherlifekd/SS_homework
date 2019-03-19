import os
import re
from app.ask import ask


def file(files_name, mod, string_for_count=None, string_for_search=None, string_for_replace=None):

    BASE_DIR = os.path.join(os.getcwd(), files_name)

    if mod.lower() == 'c':
        try:
            with open(BASE_DIR, 'r') as file:
                text = file.read()
                return print(len(re.findall(f'(?={string_for_count})', text)))
        except FileNotFoundError:
            return print('File Not Found')
    elif mod.lower() == 'r':
        try:
            with open(BASE_DIR) as file:
                text = file.read()

            new_text = text.replace(string_for_search, string_for_replace)

            with open(BASE_DIR, 'w') as file:
                file.write(new_text)
        except FileNotFoundError:
            return print('File Not Found')


def check_files(args):
    while True:
        if args.mod == 'c' and args.files_name != 'def' and args.string_for_count != 'def':
            file(args.files_name, args.mod, args.string_for_count)
            args.mod = 'def'
        elif args.mod == 'r' and args.files_name != 'def' and args.string_for_search != 'def' \
                and args.string_for_replace != 'def':
            file(args.files_name, args.mod, string_for_search=args.string_for_search,
                 string_for_replace=args.string_for_replace)
            args.mod = 'def'
        else:
            mod = input('Which mod do you want to choose? (type C to count / type R to replace '
                        '/ type anything else to exit): ').lower()
            if mod == 'c':
                try:
                    direction_count = input('<direction of your file>, <counted string>: ').replace(' ', '') \
                        .split(',')
                    file(direction_count[0], mod, direction_count[1])
                except IndexError:
                    print('Enter the correct parameters')
                    continue
            elif mod == 'r':
                try:
                    direction_replace = input(
                        '<direction of your file>, <search string>, <replace string>: ').replace \
                        (' ', '').split(',')
                    file(direction_replace[0], mod, string_for_search=direction_replace[1],
                         string_for_replace=direction_replace[2])
                except IndexError:
                    print('Enter the correct parameters')
                    continue
            else:
                break

        if ask():
            continue
        else:
            break
