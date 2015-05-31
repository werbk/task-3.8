# -*- coding: utf-8 -*-
from group_lib import Group
from tests_contract.contract_lib import connection


def test_create_group(app):
    """Validation of correct create test group (All field fill up)"""


    app.group.create(Group(group_name='test', group_header='test', group_footer='test'))
    app.group.click_group_page()
    app.group.delete_first_group()


def test_create_group_name(app):
    """Validation of correct create test group (Only group name fill up)"""

    app.group.create(Group(group_name='test'))
    app.group.click_group_page()
    app.group.delete_first_group()


def test_edit_group(app):
    """Validation of correct edit group (all field updated)"""

    app.group.create(Group(group_name='test'))
    app.group.click_group_page()
    app.group.edit_group(Group(group_name='testtest', group_header='testtest', group_footer='testtest'))
    app.group.delete_first_group()


