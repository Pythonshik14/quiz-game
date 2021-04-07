from random import *
from time import sleep
from selenium import webdriver
import requests

def load_image(search):
    url = "https://yandex.ru/images/search?from=tabbar&text="

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=r"C:\Users\user\PycharmProjects\ELAN\ParserWiki\chromedriver.exe",
                               options=options)

    browser.get(url=url+search+"картинки")
    sleep(1)
    images = browser.find_elements_by_class_name('serp-item__link')
    browser.get(images[randint(0, len(images)-1)].get_attribute('href'))
    url_image = browser.find_element_by_class_name("MMImage-Origin").get_attribute('src')
    search_image = requests.get(url_image)
    option_img = open("image_" + search + ".jpg", "wb")
    option_img.write(search_image.content)
    search_image.close()
