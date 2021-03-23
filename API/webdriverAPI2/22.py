from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# actions = ActionChains(driver)

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

countries = {
    "Italy": "Rome",
    "Spain": "Madrid",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "South Korea": "Seoul",
    "Sweden": "Stockholm",
    "United States": "Washington",
}

for country in countries:
    country_box = driver.find_element_by_xpath(f"//div[.='{country}']")
    capital_box = driver.find_element_by_xpath(f"//div[.='{countries[country]}' and contains(@id, 'box')]")
    # actions.drag_and_drop(capital_box, country_box).perform()
    # actions.reset_actions()
    ActionChains(driver).drag_and_drop(capital_box,country_box).perform()