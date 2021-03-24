"""
poium 测试库的使用
elem_id = NewPageElement(id_=‘id’)
elem_name = NewPageElement(name=‘name’)
elem_class = NewPageElement(class_name=‘class’)
elem_tag = NewPageElement(tag=‘input’)
elem_link_text = NewPageElement(link_text=‘this_is_link’)
elem_partial_link_text = NewPageElement(partial_link_text=‘is_link’)
elem_xpath = NewPageElement(xpath=’//*[@id=“kk”]’)
elem_css = NewPageElement(css=’#id’)
"""
from poium import Page
from poium.u2 import PageElement


class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = PageElement(id_="kw", describe="输入框")
    search_button = PageElement(id_="su", describe="百度一下按钮")

