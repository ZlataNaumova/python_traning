# -*- coding: utf-8 -*-
import time
from model.group import Group



def test_add_group(app):
    old_groups = app.group.get_group_list()
    add_group = Group(name="group_test", header="12", footer="112")
    app.group.create(add_group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(add_group)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) #урок 4_3
    #time.sleep(2)



#def test_empty_group(app):
 #   old_groups = app.group.get_group_list()
 #   add_group = Group(name="", header="", footer="")
 #   app.group.create(add_group)
 #   new_groups = app.group.get_group_list()
 #   assert len(old_groups) + 1 == len(new_groups)
 #   old_groups.append(add_group)
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
