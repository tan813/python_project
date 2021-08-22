"""
poium 测试库的使用
elem_id = Element(id_=‘id’)
elem_name = Element(name=‘name’)
elem_class = Element(class_name=‘class’)
elem_tag = Element(tag=‘input’)
elem_link_text = Element(link_text=‘this_is_link’)
elem_partial_link_text = Element(partial_link_text=‘is_link’)
elem_xpath = Element(xpath=’//*[@id=“kk”]’)
elem_css = Element(css=’#id’)
"""
from poium import Page, Element


class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = Element(id_="kw", timeout=3, describe="输入框")
    search_button = Element(id_="su", timeout=3, describe="百度一下按钮")

