from selenium import webdriver
from fixture.session import SessionHelper

class ApplicationGroup:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def create_group(self, group_info):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("new").click()
        # fill group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_info.name)
        # fill group header
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_info.header)
        # fill group footer
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_info.footer)
        wd.find_element_by_id("content").click()
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")



    def destroy(self):
        self.wd.quit()