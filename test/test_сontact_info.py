import re

def test_name_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
    print(contact_from_home_page.address)
    assert contact_from_home_page.address == merge_address_like_on_home_page(contact_from_edit_page)

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


'''def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_list_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
    assert contact_from_edit_page.mobile_number == contact_from_view_page.mobile_number
    assert contact_from_edit_page.home_number == contact_from_view_page.home_number
    assert contact_from_edit_page.work_number == contact_from_view_page.work_number
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2'''


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.address]))))
