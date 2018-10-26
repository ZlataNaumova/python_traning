
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_contact_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_name("submit").click()
        self.return_to_contact_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        driver.find_element_by_name(field_name).click()
        driver.find_element_by_name(field_name).clear()
        driver.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.return_to_contact_home_page()
        self.select_contact_by_index(index)
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.accept_next_alert = True
        #self.return_to_contact_home_page()
        self.group_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def count( self ):
        driver = self.app.driver
        self.return_to_contact_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    contacts_cache = None
# кааак?
    def get_contacts_list(self):
        if self.contacts_cache is None:
            driver = self.app.driver
            self.return_to_contact_home_page()
            self.contacts_cache = []
            for element in driver.find_elements_by_name("entry"):
                text = element.find_element_by_name#?????????
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Contact(firstname=text, id=id))
        return list(self.group_cache)
