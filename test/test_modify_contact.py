from model.contact_info import ContactInfo

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    app.contact.modify_first_contact(ContactInfo(firstname="Ann", company="New company", title="New title", amonth="October", notes=""))

def test_modify_contact_details(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    app.contact.modify_contact_details(ContactInfo(firstname="Annuta", company="", title= "", amonth="July", notes="New notes"))
