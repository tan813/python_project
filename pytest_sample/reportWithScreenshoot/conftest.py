from datetime import datetime

import pytest
from py._xmlgen import html
from selenium import webdriver

driver = None


# 环境准备及清理，会话级别，自动调用
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.hookwrapper  # 也可以用@pytest.hookimpl(hookwrapper=True) 两者作用相同
# 此钩子函数在setup(初始化的操作)，call（测试用例执行时），teardown（测试用例执行完毕后的处理）都会执行一次
# 每次都会返回的 Result 对象和 TestReport 对象，以及对象属性。
def pytest_runtest_makereport(item, call):
    # outcome = yield
    # report = outcome.get_result()
    # report.description = str(item.function.__doc__)
    pytest_html = item.config.pluginmanager.getplugin('html')
    # 获取钩子方法的调用结果（Result对象）
    outcome = yield
    # 从调用结果获取测试报告
    report = outcome.get_result()
    # 添加用例描述信息
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    # 只关注用例本身的执行结果，添加判断
    if report.when == 'call':
        # xfail显式的声明一个用例会失败，如果确实失败，则测试结果显示为通过
        xfail = hasattr(report, 'wasxfail')
        # 显示声明用例失败并跳过或用例执行失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen = _capture_screenshot()
            extra.append(pytest_html.extras.png(screen))
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Failure TestCase</div>'))
        report.extra = extra

    """
        报告中的截图点击不能打开放大查看？？？
        if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            print("File Name:"+file_name)
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img id= "img" src="data:image/png;base64,%s" alt="screenshot" ' \
                       'style="width:600px;height:300px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img

                extra.append(pytest_html.extras.html(html))
    report.extra = extra
    report.description = str(item.function.__doc__)
    """

# 截图
def _capture_screenshot():
    return driver.get_screenshot_as_base64()


# 修改报告标题
def pytest_html_report_title(report):
    report.title = "xx项目测试报告"


# 添加summary信息
def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear() # 清空summary中的内容
    prefix.extend([html.p("所属部门: xxx")])
    prefix.extend([html.p("测试执行人: xxx")])


# 添加Environment信息
def pytest_configure(config):
    # config._metadata.clear()
    config._metadata['测试项目'] = "测试百度官网搜索"
    config._metadata['测试地址'] = "https://www.baidu.com/"


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    # 添加用例描述
    cells.insert(2, html.th('Description'))
    # 添加时间
    # cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    # 删除最后links列的内容
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    # 添加用例描述
    cells.insert(2, html.td(report.description))
    # 添加时间
    # cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    # 删除最后links列的内容
    cells.pop()
