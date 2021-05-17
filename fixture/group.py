

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group_info):
        wd = self.app.wd
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

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()