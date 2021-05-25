from model.group_info import GroupInfo

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(GroupInfo(name="test"))
    app.group.delete_first_group()
