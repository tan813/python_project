# -*- coding: utf-8 -*-
"""
@Author   : tanjinbai
@Time     : 2021-08-25 23:06
@Function : pytest框架conftest.py配置文件,存放fixture函数及本地插件
"""
import pytest
from py._xmlgen import html
from selenium import webdriver


# 用例执行前自动调用，整个conftest.py所在目录中调用一次
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    打开退出浏览器
    :return: driver
    """
    # global声明全局变量driver，可在函数内部对函数外的变量赋值操作
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    钩子函数在setup(初始化),call（测试用例执行）,teardown（测试用例执行完毕）阶段各执行一次
    每次都返回钩子函数的调用结果Result对象和测试报告TestReport对象,以及对象的属性
    :param item: 测试用例
    :param call: 测试步骤
    """
    pytest_html = item.config.pluginmanager.getplugin('html')

    # 获取钩子方法的调用结果
    outcome = yield

    # 从调用结果获取测试报告
    report = outcome.get_result()

    # 添加用例描述信息(用例方法下用“注释的内容)
    report.description = str(item.function.__doc__)

    # 获取测试报告的extra属性，存在则返回、不存在返回[]
    extra = getattr(report, 'extra', [])

    # @pytest.mark.skip标记用例为skip，在setup阶段report.skipped=True
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')

        # @pytest.mark.xfail标记用例失败并跳过/用例执行失败,截图
        if (report.skipped and xfail) or (report.failed and not xfail):
            casePath = report.nodeid.replace("::", "_") + ".png"
            capture_screenshot(casePath)
            if casePath:
                html = '<div><img src="%s" alt="screenshot" style="width:380px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % casePath
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """
    添加Results列头信息
    :param cells:
    """
    # 添加用例描述
    cells.insert(1, html.th('Description'))
    # 添加时间
    # cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    # 删除最后links列(该列无内容)
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """
    添加Results列表中的内容
    :param report:
    :param cells:
    """
    # 添加用例描述
    cells.insert(1, html.td(report.description))
    # 添加时间
    # cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    # 删除最后links列的内容
    cells.pop()


def capture_screenshot(file_name):
    """
    调get_screenshot_as_file()截图
    :param file_name: 图片名称
    :return:
    """

    # 存放图片的路径
    img_dir = 'report/' + file_name
    return driver.get_screenshot_as_file(img_dir)


def pytest_html_report_title(report):
    """
    修改报告标题
    :param report: 测试报告
    """
    report.title = "xx项目测试报告"


def pytest_html_results_summary(prefix, summary, postfix):
    """
    添加summary信息
    :param prefix:
    :param summary:
    :param postfix:
    """
    prefix.extend([html.p("所属部门: xxx")])
    prefix.extend([html.p("测试执行人: xxx")])


def pytest_configure(config):
    """
    添加Environment信息
    :param config:
    """
    config._metadata['测试项目'] = "测试百度官网搜索"
    config._metadata['测试地址'] = "https://www.baidu.com/"


def pytest_collection_modifyitems(items):
    """
    控制台ids 中文unicode编码转换
    pytest-html源码中已做了转换，调此函数则报告中Test列内容会乱码
    :param items: 测试用例
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
