def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.session.logout()

def test_edit_contact_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact_details()
    app.session.logout()