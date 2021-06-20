# -*- coding: utf-8 -*-
from model.contact_info import ContactInfo

def test_add_contact(app):
    contact = ContactInfo(firstname="Anna", middlename="Alexseevna", lastname="Pankova", nickname="annutahse12",
                    title="task 3!", company="testing", address="localhost",
                    mobile_number="+79161234567", home_number="1234567", work_number="+456", fax="+123",
                    email="test@mail.com",
                    bday="15", bmonth="October", byear="1995",
                    aday="13", amonth="September", ayear="2012",
                    address2="moscow", notes="task 7", phone2="+456123789")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

'''
def test_add_empty_contact(app):
    contact = ContactInfo(firstname="empty contact", lastname="")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)
'''