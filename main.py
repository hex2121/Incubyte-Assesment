from selenium import webdriver
from Pages import HomePage
from Config.config import *



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(website_link)
    HomePage(driver=driver).click_create_account()
