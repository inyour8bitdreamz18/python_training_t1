from model.contact_info import ContactInfo

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactInfo(firstname="Ann", company="New company", title="New title", amonth="October", notes="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

def test_modify_contact_details(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactInfo(firstname="Annuta", company="", title= "", amonth="July", notes="New notes")
    contact.id = old_contacts[0].id
    app.contact.modify_contact_details(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

