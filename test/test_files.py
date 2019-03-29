import unittest
from unittest.mock import patch
import argparse
from app.files import files_func


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic
class TestFiles(unittest.TestCase):
    class FileObject:

        def __init__(self, string=None):
            self.value = string
            self.was_read_called = False

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def read(self, *ignore):
            if not self.was_read_called:
                self.was_read_called = True
                return self.value
            else:
                return False

        def write(self, data):
            if self.value:
                self.value += data
            else:
                self.value = data

        def get_value(self):
            return self.value

    def mock_open(*ignore):
        return TestFiles.FileObject(
            'aaaa nice aaa aa aaaaaaaaakka aaaaa nice')

    # TEST COUNT
    @patch('builtins.open', mock_open)
    def test_files_correct_params_mod_c(self):
        args = argparse.Namespace(files_name='*ignore', mod='c', string_for_count='aa')
        self.assertEqual(files_func(args), 18)

    @patch('builtins.open', mock_open)
    def test_files_correct_params_not_existing_string(self):
        args = argparse.Namespace(files_name='*ignore', mod='c', string_for_count='ffff')
        self.assertEqual(files_func(args), 0)

    @patch('builtins.open', mock_open)
    def test_files_incorrect_params_default(self):
        args = argparse.Namespace(files_name='*ignore', mod='c', string_for_count='def',
                                  string_for_replace='def', string_for_search='def')
        self.assertEqual(files_func(args), False)

    def test_files_incorrect_params_file_not_found(self):
        args = argparse.Namespace(files_name='testcount123', mod='c', string_for_count='aa')
        self.assertEqual(files_func(args), 'File Not Found')

    @patch('builtins.open', mock_open)
    def test_files_incorrect_params_None(self):
        args = argparse.Namespace(files_name='*ignore', mod=None, string_for_count='aa')
        self.assertEqual(files_func(args), False)

    # TEST REPLACE
    RESULT_STRING = 'aaaa hi aaa aa aaaaaaaaakka aaaaa hi'

    @patch('builtins.open', mock_open)
    def test_files_correct_params_mod_r(self):
        args = argparse.Namespace(files_name='*ignore', mod='r', string_for_search='nice', string_for_replace='hi',
                                  string_for_count='def')
        self.assertEqual(files_func(args), 'Done. Check your file')

    @patch('builtins.open', mock_open)
    def test_files_correct_params_string_not_found(self):
        args = argparse.Namespace(files_name='*ignore', mod='r', string_for_search='hello', string_for_replace='hi',
                                  string_for_count='def')
        self.assertEqual(files_func(args), 'The string is not found')

    def test_files_correct_params_file_not_found(self):
        args = argparse.Namespace(files_name='file12', mod='r', string_for_search='nice', string_for_replace='hi',
                                  string_for_count='def')
        self.assertEqual(files_func(args), 'File Not Found')


if __name__ == 'main':
    unittest.main()
