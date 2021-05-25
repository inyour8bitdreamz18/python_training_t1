# -*- coding: utf-8 -*-
from model.group_info import GroupInfo

def test_add_new_group(app):
    app.group.create(GroupInfo(name="test group", header="test header", footer="test footer"))

def test_add_empty_group(app):
    app.group.create(GroupInfo(name="", header="", footer=""))
