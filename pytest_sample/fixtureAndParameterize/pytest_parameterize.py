# pytest 参数化

import math

import pytest


@pytest.mark.parametrize(
    "base,exponent,expected",
    [(2, 2, 4),
     (2, 3, 8),
     (1, 9, 9)
     ],
    ids=['case1', 'case2', 'case3']
)
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected
    print('finished!')


if __name__ == '__main__':
    # 生成xml测试报告
    # pytest.main(['-v','--junit-xml=./report/log.xml', '.'])

    # 生成html测试报告
    pytest.main(['-v', '--html=./report/result.html', './pytest_parameterize.py'])

    # 失败重跑3次，间隔3s（或使用装饰器）
    # pytest.main(['-v', '--html=./report/result.html', '--reruns','3','--reruns-delay', '3' , './pytest_parameterize.py'])
