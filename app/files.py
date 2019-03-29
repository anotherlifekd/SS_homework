import os
import re
import argparse
from app.ask import ask


def check_args(args):
    if args.files_name is not None and args.mod is not None and args.string_for_count is not None \
            and args.mod == 'c' and args.files_name != 'def' and args.string_for_count != 'def':
        return True
    elif args.files_name is not None and args.mod is not None and args.string_for_replace is not None \
            and args.string_for_search is not None and args.mod == 'r' and args.files_name != 'def' \
            and args.string_for_search != 'def' and args.string_for_replace != 'def':
        return True
    else:
        return False


def files_func(args):
    def file():
        BASE_DIR = os.path.join(os.getcwd(), args.files_name)

        if args.mod.lower() == 'c':
            try:
                with open(BASE_DIR, 'r') as f:
                    text = f.read()
                    return len(re.findall(f'(?={args.string_for_count})', text))
            except FileNotFoundError:
                return 'File Not Found'
            except IsADirectoryError:
                return 'Is a directory'
        elif args.mod.lower() == 'r':
            try:
                with open(BASE_DIR) as f:
                    text = f.read()
                    if args.string_for_search not in text:
                        return 'The string is not found'

                new_text = text.replace(args.string_for_search, args.string_for_replace)

                with open(BASE_DIR, 'w') as f:
                    f.write(new_text)
                    return 'Done. Check your file'
            except FileNotFoundError:
                return 'File Not Found'
            except IsADirectoryError:
                return 'Is a directory'

    if check_args(args):
        return file()
    else:
        return False


def check_files(args):
    while True:
        if check_args(args):
            print(files_func(args))
            args.mod = 'def'
        else:
            mod = input('Which mod do you want to choose? (type C to count / type R to replace '
                        '/ type anything else to exit): ').lower()
            if mod == 'c':
                direction_count = input('<direction of your file>, <counted string>: ').replace(' ', '').split(',')
                args = argparse.Namespace(files_name=direction_count[0], mod=mod, string_for_count=direction_count[1],
                                          string_for_search='def', string_for_replace='def')
                if len(direction_count) > 2:
                    print('Enter the correct parameters')
                    args.string_for_count = 'def'
                    continue
                print(files_func(args))
                args.string_for_count = 'def'
            elif mod == 'r':
                direction_replace = input('<direction of your file>, <search string>, <replace string>: ')\
                    .replace(' ', '').split(',')
                if len(direction_replace) > 3:
                    print('Enter the correct parameters')
                    args.string_for_search = args.string_for_replace = 'def'
                    continue
                args = argparse.Namespace(files_name=direction_replace[0], string_for_search=direction_replace[1],
                                          string_for_replace=direction_replace[2], mod=mod, string_for_count='def')
                print(files_func(args))
                args.string_for_search = args.string_for_replace = 'def'
            else:
                break

        if ask():
            continue
        else:
            break
