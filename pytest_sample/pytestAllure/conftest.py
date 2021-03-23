import pytest
from selenium import webdriver
import os
import allure

_driver = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


_driver = None


@pytest.fixture(scope='session')
def browser():
    global _driver
    print('\n赋值前driver is :%s' % _driver)
    # if _driver is None:
    #     _driver = webdriver.Chrome()
    #     print('\n赋值后driver is :%s' % _driver)
    _driver = webdriver.Chrome()
    print('\n赋值后driver is :%s' % _driver)
    yield _driver
    _driver.quit()
