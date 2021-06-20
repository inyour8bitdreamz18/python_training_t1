from model.contact_info import ContactInfo
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="Alex", lastname='Ivanov'))
        app.contact.create(ContactInfo(firstname="Sasha", lastname='Petrov'))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) -1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    print(app.contact.count())
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test contact 1"))
        app.contact.create(ContactInfo(firstname="test contact 2"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(new_contacts) == app.contact.count()
    old_contacts = []
    assert old_contacts == new_contacts

