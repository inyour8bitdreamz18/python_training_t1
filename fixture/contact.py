
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact_info):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # add first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_info.firstname)
        wd.find_element_by_name("theform").click()
        # add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_info.middlename)
        wd.find_element_by_name("theform").click()
        # add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_info.lastname)
        wd.find_element_by_name("theform").click()
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_info.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("theform").click()
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_info.title)
        # add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_info.company)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_info.address)
        wd.find_element_by_name("theform").click()
        # add home number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_info.home_number)
        # add mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_info.mobile_number)
        # add work number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_info.work_number)
        # add fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_info.fax)
        # add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_info.email)
        wd.find_element_by_name("theform").click()
        # add birthday date
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_info.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_info.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_info.byear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("theform").click()
        # add anniversary date
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_info.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_info.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_info.ayear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("theform").click()
        # add address 2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_info.address2)
        wd.find_element_by_name("theform").click()
        # add phone number 2
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_info.phone2)
        wd.find_element_by_name("theform").click()
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_info.notes)
        # submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_table(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()