import unittest
import argparse
from app.analytics import analytics_func


class TestAnalytics(unittest.TestCase):

    EXPECT = ('YES', 'NO')

    def test_analytics_correct_params1(self):
        args = argparse.Namespace(envelope_a='5', envelope_b='5', envelope_c='4', envelope_d='4')
        self.assertEqual(analytics_func(args), self.EXPECT[0])

    def test_analytics_correct_params2(self):
        args = argparse.Namespace(envelope_a='5', envelope_b='5', envelope_c='6', envelope_d='4')
        self.assertEqual(analytics_func(args), self.EXPECT[1])

    def test_analytics_correct_params3(self):
        args = argparse.Namespace(envelope_a='5.3', envelope_b='4.0', envelope_c='3.1', envelope_d='3.9')
        self.assertEqual(analytics_func(args), self.EXPECT[0])

    def test_analytics_incorrect_params_str(self):
        args = argparse.Namespace(envelope_a='sdf', envelope_b='4.0', envelope_c='3.1', envelope_d='3.9')
        self.assertFalse(analytics_func(args))

    def test_analytics_incorrect_params_None(self):
        args = argparse.Namespace(envelope_a='5', envelope_b='4.0', envelope_c=None, envelope_d='3.9')
        self.assertFalse(analytics_func(args))

    def test_analytics_incorrect_params_negative_number(self):
        args = argparse.Namespace(envelope_a='5', envelope_b='4.0', envelope_c='-2', envelope_d='3.9')
        self.assertFalse(analytics_func(args))

    def test_analytics_incorrect_params_zero(self):
        args = argparse.Namespace(envelope_a='5', envelope_b='0', envelope_c='3', envelope_d='3.9')
        self.assertFalse(analytics_func(args))


if __name__ == 'main':
    unittest.main()
