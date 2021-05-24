from model.group_info import GroupInfo
def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(GroupInfo(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(GroupInfo(header="New header"))
    app.session.logout()