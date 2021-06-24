from model.contact_info import ContactInfo
from random import randrange

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = ContactInfo(firstname="Svetlana", lastname='Nova', company="New company", title="New title", amonth="October",notes="")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)


def test_modify_some_contact_details(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test", middlename="test"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    index = randrange(len(old_contacts))
    contact = ContactInfo(firstname="Annuta", company="", title= "", amonth="July", notes="New notes")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index_details(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

