import unittest

from unittest_sample.unittest_test import test_calculator

if __name__ =='__main__':
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTest(loader.loadTestsFromModule(test_calculator))
    runner = unittest.TextTestRunner()
    runner.run(suit)