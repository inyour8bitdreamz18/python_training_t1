from selenium.webdriver.support.ui import Select
from model.contact_info import ContactInfo
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.change_field_value("firstname", contact_info.firstname)
        self.change_field_value("middlename", contact_info.middlename)
        self.change_field_value("lastname", contact_info.lastname)
        self.change_field_value("nickname", contact_info.nickname)
        self.change_field_value("title", contact_info.title)
        self.change_field_value("company", contact_info.company)
        self.change_field_value("address", contact_info.address)
        self.change_field_value("home", contact_info.home_number)
        self.change_field_value("mobile", contact_info.mobile_number)
        self.change_field_value("work", contact_info.work_number)
        self.change_field_value("fax", contact_info.fax)
        self.change_field_value("email", contact_info.email)
        self.change_field_value("email2", contact_info.email2)
        self.change_field_value("email3", contact_info.email3)
        self.change_field_value("homepage", contact_info.homepage)
        self.select_field_value("bday", contact_info.bday)
        self.select_field_value("bmonth", contact_info.bmonth)
        self.change_field_value("byear", contact_info.byear)
        self.select_field_value("aday", contact_info.aday)
        self.select_field_value("amonth", contact_info.amonth)
        self.change_field_value("ayear", contact_info.ayear)
        self.change_field_value("group", contact_info.group)
        self.change_field_value("address2", contact_info.address2)
        self.change_field_value("phone2", contact_info.phone2)
        self.change_field_value("notes", contact_info.notes)
        # submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contact_table()
        self.contact_cache = None


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).click()
            Select(wd.find_element_by_name(fieldname)).select_by_visible_text(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def modify_contact_by_index_details(self, contact_info, index):
        wd = self.app.wd
        self.open_contact_table()
        self.select_contact_by_index(index)
        #open contact details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        #change some field values
        self.change_field_value("firstname", contact_info.firstname)
        self.change_field_value("company", contact_info.company)
        self.change_field_value("title", contact_info.title)
        self.select_field_value("amonth", contact_info.amonth)
        self.change_field_value("notes", contact_info.notes)
        #submit editing
        wd.find_element_by_name("update").click()
        self.return_to_contact_table()
        self.contact_cache = None

    def modify_contact_details(self):
        self.modify_contact_by_index_details(0)

    def modify_contact_by_index(self, contact_info, index):
        wd = self.app.wd
        self.open_contact_table()
        # click on edit contact by index
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # change some field values
        self.change_field_value("firstname", contact_info.firstname)
        self.change_field_value("lastname", contact_info.lastname)
        self.change_field_value("title", contact_info.title)
        self.select_field_value("amonth", contact_info.amonth)
        self.change_field_value("notes", contact_info.notes)
        #update modified data
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact_table()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_table()
        self.select_contact_by_index(index)
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_table()
        # select first contact
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_table(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_contact_table(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_table()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_table()
            self.contact_cache = []
            if self.count() != 0:
                for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                    cells = element.find_elements_by_tag_name("td")
                    lastname = element.find_element_by_css_selector('td:nth-of-type(2)').text
                    firstname = element.find_element_by_css_selector('td:nth-of-type(3)').text
                    id = element.find_element_by_name('selected[]').get_attribute('value')
                    address = cells[3].text
                    print(address)
                    all_emails = cells[4].text
                    all_phones = cells[5].text
                    self.contact_cache.append(ContactInfo(firstname=firstname, lastname=lastname, id=id,
                                                          all_phones_from_home_page=all_phones,
                                                          all_emails_from_home_page=all_emails,
                                                          address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return ContactInfo(firstname=firstname, lastname=lastname, id=id,
                           home_number=home_number, work_number=work_number,
                           mobile_number=mobile_number, phone2=phone2,
                           email=email, email2=email2, email3=email3,
                           address=address)

    def get_contact_list_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return ContactInfo(home_number=home_number, work_number=work_number,
                           mobile_number=mobile_number, phone2=phone2)