from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_firstname(contact_info)
        self.fill_middlename(contact_info)
        self.fill_lastname(contact_info)
        self.fill_nickname(contact_info)
        self.fill_title(contact_info)
        self.fill_company(contact_info)
        self.fill_address(contact_info)
        self.fill_home_number(contact_info)
        self.fill_mobile_number(contact_info)
        self.fill_work_number(contact_info)
        self.fill_fax(contact_info)
        self.fill_email(contact_info)
        #fill birthday date
        self.fill_bday(contact_info)
        self.fill_bmonth(contact_info)
        self.fill_byear(contact_info)
        #fill anniversary date
        self.fill_aday(contact_info)
        self.fill_amonth(contact_info)
        self.fill_ayear(contact_info)
        #
        self.fill_address2(contact_info)
        self.fill_phone2(contact_info)
        self.fill_notes(contact_info)
        # submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_notes(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_info.notes)

    def fill_phone2(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_info.phone2)

    def fill_address2(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_info.address2)

    def fill_ayear(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_info.ayear)

    def fill_amonth(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_info.amonth)
        wd.find_element_by_name("amonth").click()

    def fill_aday(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_info.aday)
        wd.find_element_by_name("aday").click()

    def fill_byear(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_info.byear)

    def fill_bmonth(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_info.bmonth)
        wd.find_element_by_name("bmonth").click()

    def fill_bday(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_info.bday)
        wd.find_element_by_name("bday").click()

    def fill_email(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_info.email)

    def fill_fax(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_info.fax)

    def fill_work_number(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_info.work_number)

    def fill_mobile_number(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_info.mobile_number)

    def fill_home_number(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_info.home_number)

    def fill_address(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_info.address)

    def fill_company(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_info.company)

    def fill_title(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_info.title)

    def fill_nickname(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_info.nickname)

    def fill_lastname(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_info.lastname)

    def fill_middlename(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_info.middlename)

    def fill_firstname(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_info.firstname)

    def modify_contact_details(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        #open contact details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        #submit editing
        wd.find_element_by_name("modifiy").click()
        self.modify_first_contact(contact_info)

    def modify_first_contact(self, contact_info):
        wd = self.app.wd
        self.open_contact_table()
        # click on edit first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.submit_modified_field()
        # edit firstname
        self.fill_firstname(contact_info)
        self.submit_modified_field()
        # edit company
        self.fill_company(contact_info)
        self.submit_modified_field()
        # edit title
        self.fill_title(contact_info)
        self.submit_modified_field()
        # edit anniversary month
        self.fill_amonth(contact_info)
        self.submit_modified_field()
        # edit notes
        self.fill_notes(contact_info)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contact_table()

    def submit_modified_field(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@action='edit.php']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_table()
        # select first contact
        wd.find_element_by_name("selected[]").click()
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
        self.accept_nest_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_table()



    def open_contact_table(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()