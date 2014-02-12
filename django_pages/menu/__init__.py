# -*- encoding: utf-8 -*-

from .models import Menu


def has_other_menu():
    """
    Checks if there are more than one
    menu in the system.

    :return: True or False
    :rtype: :py:obj:`bool`
    """

    if Menu.objects.exclude(pk=0):
        return True

    return False


def get_other_menuitems():
    """
    returns other menu items

    each menu pk will be dict key
    {0: QuerySet, 1: QuerySet
    """
    menuitems = {}
    all_objects = Menu.objects.all()

    for obj in all_objects:
        menuitems[obj.pk] = obj.menuitem_set.all()

    return menuitems
