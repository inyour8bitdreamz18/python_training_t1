from model.contact_info import ContactInfo

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactInfo(firstname="test contact 1"))
    app.contact.delete_first_contact()

def test_delete_all_contacts(app):
    if app.group.count() <= 1:
        app.contact.create(ContactInfo(firstname="test contact 2"))
    app.contact.delete_all_contacts()
