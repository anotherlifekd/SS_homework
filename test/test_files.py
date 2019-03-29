import unittest
import argparse
from app.files import files_func


class TestAnalytics(unittest.TestCase):

    EXPECT = ('YES', 'NO')

    # def test_analytics_correct_params1(self):
    #     args = argparse.Namespace(envelope_a='5', envelope_b='5', envelope_c='4', envelope_d='4')
    #     self.assertEqual(analytics_func(args), self.EXPECT[0])



if __name__ == 'main':
    unittest.main()
