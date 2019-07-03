from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

global link
link = input("Link: ")

def spam():
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(link)
    elem = driver.find_element_by_name("text")
    elem.send_keys(".")
    driver.find_element_by_id("send-button").click()
    driver.quit()

    return spam()


spam()
