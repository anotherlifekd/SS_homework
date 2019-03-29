#!/usr/bin/env python3
import unittest

if __name__ == "main":
    all_tests = unittest.TestLoader().discover('../test', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)