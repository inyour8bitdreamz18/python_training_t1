from model.group_info import GroupInfo
def test_modify_group_name(app):
    app.group.modify_first_group(GroupInfo(name="New group"))

def test_modify_group_header(app):
    app.group.modify_first_group(GroupInfo(header="New header"))
