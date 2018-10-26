from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__( self ):
        self.driver = self.driver = webdriver.Chrome(executable_path=r'C:\pselenium\chromedriver_win32\chromedriver.exe')
            #webdriver.Firefox(executable_path=r'C:\pselenium\geckodriver-v0.19.1-win64\geckodriver.exe')
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        #self.driver.implicitly_wait(5)
        driver.get("http://localhost/addressbook/")

    def desrtoy(self):
        self.driver.quit()

