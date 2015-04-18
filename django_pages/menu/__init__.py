# -*- encoding: utf-8 -*-

from .models import Menu


def get_main_menuitems(current_page_url, page, preview=False):
    """
    Returns menuitem set for specified page
    if preview = True, it displays non-active menuitems
    """
    menuitems_orig = page.link.lang.menuitem_set
    menuitems = menuitems_orig.order_by('position').filter(menu__id=1)

    # filter active pages if we're not previewing
    if not preview:
        menuitems = menuitems.filter(page__active=True)

    # build a list with menuitems, querysets can't be extended
    new_menuitems = []
    for menuitem in menuitems:
        menuitem.current = menuitem.is_current(current_page_url)
        new_menuitems.append(menuitem)

    new_menuitems.extend(
        menuitems_orig.order_by('position').filter(
            url__icontains='http://', menu__id=1
        )
    )

    return sorted(new_menuitems, cmp=lambda x, y: cmp(x.position, y.position))


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
    {0: QuerySet, 1: QuerySet, ..}
    """
    menuitems = {}
    all_objects = Menu.objects.all()

    for obj in all_objects:
        menuitems[obj.pk] = obj.menuitem_set.all()

    return menuitems
