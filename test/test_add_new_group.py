# -*- coding: utf-8 -*-
import pytest
from model.group_info import GroupInfo
from fixture.application_group import ApplicationGroup

@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_group(GroupInfo(name="test group", header="test header", footer="test footer"))
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_group(GroupInfo(name="", header="", footer=""))
    app.logout()
