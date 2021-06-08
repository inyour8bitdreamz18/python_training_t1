from model.group_info import GroupInfo

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(GroupInfo(name="test"))
    old_groups = app.group.get_group_list()
    print(old_groups)
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    print(new_groups)
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
