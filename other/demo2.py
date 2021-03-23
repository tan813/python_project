import unittest_sample




class TestAssert(unittest_sample.TestCase):
    def test_equal(self):
        self.assertEqual(2+2,4)
        self.assertEqual("PYTHON","PYTHON")
        self.assertEqual("hello","python")

if __name__ == '__main__':
    unittest_sample.main()