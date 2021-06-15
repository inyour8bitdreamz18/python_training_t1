from model.contact_info import ContactInfo

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="Alex", lastname='Ivanov'))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test contact 1"))
        app.contact.create(ContactInfo(firstname="test contact 2"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
    old_contacts = []
    assert old_contacts == new_contacts
