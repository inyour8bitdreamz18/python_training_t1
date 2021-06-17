from model.contact_info import ContactInfo

def test_delete_first_contact(app):
    print(app.contact.count())
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="Alex", lastname='Ivanov'))
        app.contact.create(ContactInfo(firstname="Sasha", lastname='Petrov'))
    old_contacts = app.contact.get_contact_list()
    print('before deleting: {}'.format(app.contact.count()))
    app.contact.delete_first_contact()
    print('after deleting: {}'.format(app.contact.count()))
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

def test_delete_all_contacts(app):
    print(app.contact.count())
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test contact 1"))
        app.contact.create(ContactInfo(firstname="test contact 2"))
    old_contacts = app.contact.get_contact_list()
    print('before deleting: {}'.format(app.contact.count()))
    app.contact.delete_all_contacts()
    print('after deleting: {}'.format(app.contact.count()))
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == app.contact.count()
    old_contacts = []
    assert old_contacts == new_contacts
