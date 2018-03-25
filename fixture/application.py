from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\pselenium\geckodriver-v0.19.1-win64\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    



   
    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def desrtoy(self):
        self.driver.quit()

