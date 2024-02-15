from selenium import webdriver
from selenium.webdriver.common.by import By
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def option_picker(elements, money):
    prices = []
    for element in elements:
        prices.append(element.split('-')[1])
    prices = [int(price.replace(',', '')) for price in prices]
    print(prices)
    for price in list(reversed(prices)):
        if int(money.text.replace(',', '')) >= price:
            return elements[prices.index(price)]
    return False




def store_checker(money):
    store_elements = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    elements = [store_elements[num].text for num in range(len(store_elements) - 1)]
    new_elements = []
    for element in elements:
        new_elements.append(element.replace(' ', ''))

    to_buy = option_picker(new_elements, money)
    if to_buy is not False:
        buyer(to_buy)


def buyer(to_buy):
    driver.find_element(By.ID, f"buy{to_buy.split('-')[0]}").click()


def buy_check():
    money = driver.find_element(By.ID, value="money")
    store_checker(money)

timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    driver.find_element(By.ID, value="cookie").click()
    if time.time() > timeout:
        buy_check()
        timeout = time.time() + 5

