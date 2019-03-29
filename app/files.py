import os
import re
import argparse
from app.ask import ask


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

    def _check_args():
        if args.files_name is not None and args.mod is not None and args.string_for_count is not None \
                and args.mod == 'c' and args.files_name != 'def' and args.string_for_count != 'def':
            return True
        elif args.files_name is not None and args.mod is not None and args.string_for_replace is not None \
                and args.string_for_search is not None and args.mod == 'r' and args.files_name != 'def' \
                and args.string_for_search != 'def' and args.string_for_replace != 'def':
            return True
        else:
            return False

    if _check_args():
        return file()
    else:
        return False


def check_files(args):
    while True:
        if files_func(args):
            print(files_func(args))
            args.mod = 'def'
        elif files_func(args):
            print(files_func(args))
            args.mod = 'def'
        else:
            mod = input('Which mod do you want to choose? (type C to count / type R to replace '
                        '/ type anything else to exit): ').lower()
            if mod == 'c':
                try:
                    direction_count = input('<direction of your file>, <counted string>: ').replace(' ', '') \
                        .split(',')
                    args = argparse.Namespace(files_name=direction_count[0], mod=mod,
                                              string_for_count=direction_count[1], string_for_search='def',
                                              string_for_replace='def')
                    print(files_func(args))
                    args.string_for_count = 'def'
                except IndexError:
                    print('Enter the correct parameters')
                    continue
                except IsADirectoryError:
                    print('Is a directory')
                    continue
            elif mod == 'r':
                try:
                    direction_replace = input(
                        '<direction of your file>, <search string>, <replace string>: ').replace \
                        (' ', '').split(',')
                    args = argparse.Namespace(files_name=direction_replace[0], string_for_search=direction_replace[1],
                                              string_for_replace=direction_replace[2])
                    print(files_func(args))
                except IndexError:
                    print('Enter the correct parameters')
                    continue
                except IsADirectoryError:
                    print('Is a directory')
            else:
                break

        if ask():
            continue
        else:
            break
