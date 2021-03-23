import unittest

import pytest

from unittest_sample.test_dynamic.A import Failed


class TestA(unittest.TestCase):
    def test_1(self):
        try:
            assert 0
        except Exception as e:
            setattr(Failed, "skip", True)
            raise e

    # @unittest.skipIf(getattr(Failed, "skip") , "test_1失败，test_2跳过")
    def test_2(self):

        f = getattr(Failed, "skip")
        if f:
            pytest.skip()


if __name__ == '__main__':
    unittest.main()
