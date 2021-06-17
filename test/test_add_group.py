# -*- coding: utf-8 -*-
from model.group_info import GroupInfo

def test_add_new_group(app):
    group = GroupInfo(name="test group", header="test header", footer="test footer")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=GroupInfo.id_or_max) == sorted(new_groups, key=GroupInfo.id_or_max)

'''
def test_add_empty_group(app):
    group = GroupInfo(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=GroupInfo.id_or_max) == sorted(new_groups, key=GroupInfo.id_or_max)
'''