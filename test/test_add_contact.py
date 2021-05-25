# -*- coding: utf-8 -*-

from model.contact_info import ContactInfo

def test_add_contact(app):
    app.open_home_page()
    app.contact.create(
        ContactInfo(firstname="Anna", middlename="Alexseevna", lastname="Pankova", nickname="annutahse12",
                    title="task 3!", company="testing", address="localhost",
                    mobile_number="+79161234567", home_number="1234567", work_number="+456", fax="+123",
                    email="test@mail.com",
                    bday="15", bmonth="October", byear="1995",
                    aday="13", amonth="September", ayear="2012",
                    address2="moscow", notes="task 7", phone2="+456123789"))
    app.contact.open_contact_table()

