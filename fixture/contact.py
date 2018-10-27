
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page( self ):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_name("submit").click()
        self.open_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        self.select_contact_by_index(index)
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.accept_next_alert = True
        #self.return_to_contact_home_page()
        self.group_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def open_contacts_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contacts_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def count( self ):
        driver = self.app.driver
        self.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,id=id,all_phones_from_contact_page = all_phones))
                                                  #homephone=all_phones[0], mobilephone=all_phones[1],
                                                  #workphone=all_phones[2]))#, secondaryphone=all_phones[3]
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contacts_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        #secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return (Contact(firstname=firstname, lastname=lastname,id=id,
                        homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone))#, secondaryphone=secondaryphone

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contacts_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return (Contact(homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone))  # , secondaryphone=secondaryphone






