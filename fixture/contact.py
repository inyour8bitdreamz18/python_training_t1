from selenium.webdriver.support.ui import Select

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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact_details(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        self.select_first_contact()
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

    def modify_first_contact(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        # click on edit first contact
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.change_field_value("firstname", contact_info.firstname)
        self.change_field_value("title", contact_info.title)
        self.select_field_value("amonth", contact_info.amonth)
        self.change_field_value("notes", contact_info.notes)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_contact_table()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_table()
        # select first contact
        self.select_first_contact()
        # submit deletion
        self.accept_nest_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_table()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_table()
        # select first contact
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_table()

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
