from selenium import webdriver
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time


def test_add_item_to_cart_and_check_message():
    # Arrange
    url: str = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    browser: WebDriver = webdriver.Chrome()
    browser.get(url)

    in_stock_elements: List[WebElement] = browser.find_elements_by_css_selector(".instock")

    if len(in_stock_elements) == 0:
        assert False, "Expected any item to be with \"instock\" status, but no such elements found on the page"

    # Act
    browser.find_element_by_css_selector("ol li:first-child .product_pod .btn[type='submit']:not([disabled])").click()

    # Assert
    messages_first_button_text: str = browser.find_element_by_css_selector("#messages a.btn:first-child").text
    assert messages_first_button_text == "Посмотреть корзину", \
        "Expected a button with \"Посмотреть корзину\" text to appear in messages block, but no such element found"

    time.sleep(10)
    browser.quit()


test_add_item_to_cart_and_check_message()
