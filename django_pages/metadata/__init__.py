# -*- encoding: utf-8 -*-


def get_metadata(page):
    '''
    returns metadata for page

    @param page: Page object
    @return MetaData QuerySet
    '''

    if page.metadata_set:

        return page.metadata_set.metadata_set.all()

    return None
