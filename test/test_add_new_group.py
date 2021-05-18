# -*- coding: utf-8 -*-
from model.group_info import GroupInfo

def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(GroupInfo(name="test group", header="test header", footer="test footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(GroupInfo(name="", header="", footer=""))
    app.session.logout()
