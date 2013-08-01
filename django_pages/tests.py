## -*- encoding: utf-8 -*-
#
#from datetime import datetime
#
#from django.http import Http404
#from django.test import TestCase
#from django.utils.timezone import make_aware, get_current_timezone
#
#
#class ModelSiteTest(TestCase):
#
#    def setUp(self):
#
#        self.site = Site(domain='lnemec.tk', display_name='Lnemecdomain', tagline='shitt', footer='as')
#        self.site.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.site.__unicode__(), self.site.domain)
#
#
#class ModelLanguageTest(TestCase):
#
#    def setUp(self):
#
#        self.lang = Language()
#        self.lang.language = 'English'
#        self.lang.country_code = 'EN'
#        self.lang.save()
#
#        self.lang_from_db = Language.objects.get(pk=1)
#
#        self.lang2 = Language()
#        self.lang2.language = 'Czech'
#        self.lang2.country_code = 'CZ'
#        self.lang2.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.lang.__unicode__(), self.lang.language)
#
#    def test_country_code_smallcase_in_db(self):
#
#        self.assertEqual(self.lang_from_db.country_code, 'en')
#
#    def test_country_code_smallcase_after_save(self):
#
#        self.assertEqual(self.lang.country_code, 'en')
#
#    def test_first_lang_default_true(self):
#
#        self.assertTrue(self.lang_from_db.default)
#
#    def test_second_lang_default_false(self):
#
#        self.assertFalse(self.lang2.default)
#
#    def test_default_swap(self):
#
#        self.lang2.default = True
#        self.lang2.save()
#
#        self.lang = Language.objects.get(pk=1)
#
#        self.assertTrue(self.lang2.default)
#        self.assertFalse(self.lang.default)
#
#    def test_default_swap_after_delete(self):
#
#        self.lang2.delete()
#
#        self.lang = Language.objects.get(pk=1)
#
#        self.assertTrue(self.lang.default)
#
#    def test_can_be_deleted(self):
#
#        self.lang.delete()
#
#    def test_languages_empty(self):
#
#        self.lang.delete()
#        self.lang2.delete()
#
#        lang_count = Language.objects.all().count()
#
#        self.assertEqual(lang_count, 0)
#
#
#class ModelMenuTest(TestCase):
#
#    def setUp(self):
#
#        self.lang = Language(language='Czech', country_code='CZ')
#        self.lang.save()
#        self.menu = Menu(lang=self.lang, menu_name='Menu')
#        self.menu.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.menu.__unicode__(), self.menu.menu_name)
#
#
#class ModelMenuItemTest(TestCase):
#
#    def setUp(self):
#
#        self.lang = Language(language='English', country_code='EN')
#        self.lang.save()
#        self.lang2 = Language(language='Czech', country_code='CZ')
#        self.lang2.save()
#        self.menu = Menu(lang=self.lang, menu_name='Menu_english')
#        self.menu.save()
#        self.menu2 = Menu(lang=self.lang2, menu_name='Menu2_english')
#        self.menu2.save()
#
#        self.menuitem1 = MenuItem(menu=self.menu, menuitem_name='Menuitem1', url='a')
#        self.menuitem1.save()
#        self.menuitem2 = MenuItem(menu=self.menu, menuitem_name='Menuitem2', url='ag')
#        self.menuitem2.save()
#        self.menuitem3 = MenuItem(menu=self.menu, menuitem_name='Menuitem4', url='gg')
#        self.menuitem3.save()
#
#        self.page = Page(link=self.menuitem1, title='title', content='cac', active=True, index=True)
#        self.page.save()
#
#        self.menu2item1 = MenuItem(menu=self.menu2, menuitem_name='Menu2item1', url='m2i1')
#        self.menu2item1.save()
#        self.menu2item2 = MenuItem(menu=self.menu2, menuitem_name='Menu2item2', url='m2i2')
#        self.menu2item2.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.menuitem1.__unicode__(), '%s@%s' % (self.menuitem1.menuitem_name, self.menuitem1.menu.menu_name))
#
#    def test_menuitems_positions(self):
#
#        self.assertEqual(self.menuitem1.position, 1)
#        self.assertEqual(self.menuitem2.position, 2)
#        self.assertEqual(self.menuitem3.position, 3)
#
#        self.assertEqual(self.menu2item1.position, 1)
#        self.assertEqual(self.menu2item2.position, 2)
#
#    def test_get_last_position(self):
#
#        self.assertEqual(self.menuitem1.get_last_position(), 3)
#        self.assertEqual(self.menu2item2.get_last_position(), 2)
#
#    def test_is_first(self):
#
#        self.assertTrue(self.menuitem1.is_first())
#        self.assertFalse(self.menuitem3.is_first())
#        self.assertTrue(self.menu2item1.is_first())
#        self.assertFalse(self.menu2item2.is_first())
#
#    def test_is_last(self):
#
#        self.assertTrue(self.menuitem3.is_last())
#        self.assertFalse(self.menuitem2.is_last())
#        self.assertTrue(self.menu2item2.is_last())
#        self.assertFalse(self.menu2item1.is_last())
#
#    def test_position_increase(self):
#
#        self.menuitem3.increase_position()
#
#        self.assertEqual(self.menuitem3.position, 3)
#
#        self.menuitem1.increase_position()
#
#        menuitem2_id = self.menuitem2.id
#        self.menuitem2 = MenuItem.objects.get(id=menuitem2_id)
#
#        self.assertEqual(self.menuitem1.position, 2)
#        self.assertEqual(self.menuitem2.position, 1)
#
#    def test_position_decrease(self):
#
#        self.menuitem1.decrease_position()
#        self.menuitem3.decrease_position()
#
#        menuitem2_id = self.menuitem2.id
#        self.menuitem2 = MenuItem.objects.get(id=menuitem2_id)
#
#        self.assertEqual(self.menuitem1.position, 1)
#        self.assertEqual(self.menuitem3.position, 2)
#        self.assertEqual(self.menuitem2.position, 3)
#
#    def test_is_current(self):
#
#        self.assertTrue(self.menuitem1.is_current('a'))
#        self.assertTrue(self.menuitem2.is_current('ag'))
#        self.assertFalse(self.menuitem1.is_current('not current'))
#        self.assertTrue(self.menuitem1.is_current(None))
#
#
#class ModelMetaSetTest(TestCase):
#
#    def setUp(self):
#
#        self.language = Language(language='English', country_code='EN')
#        self.language.save()
#        self.metaset = MetaSet(language=self.language, name='metaset')
#        self.metaset.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.metaset.__unicode__(), self.metaset.name)
#
#
#class ModelMetaDataTest(TestCase):
#
#    def setUp(self):
#
#        self.language = Language(language='English', country_code='EN')
#        self.language.save()
#
#        self.metaset = MetaSet(language=self.language, name='metaset')
#        self.metaset.save()
#
#        self.metadata = MetaData(meta_set=self.metaset, name='keywords', content='klicova slova')
#        self.metadata.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.metadata.__unicode__(), '%s@%s' % (self.metadata.name, self.metaset.name))
#
#
#class ModelPageTest(TestCase):
#
#    def setUp(self):
#
#        self.lang = Language(language='English', country_code='EN')
#        self.lang.save()
#        self.menu = Menu(lang=self.lang, menu_name='menu')
#        self.menu.save()
#        self.menuitem = MenuItem(menu=self.menu, menuitem_name='Some Page', url='somewhere')
#        self.menuitem.save()
#
#        self.page = Page(link=self.menuitem, title='Title', content='asdf', active=True, index=True)
#        self.page.save()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.page.__unicode__(), self.page.title)
#
#    def test_have_posts(self):
#
#        self.assertFalse(self.page.have_posts())
#
#        self.post = Post(page=self.page, title='post', content='content')
#        self.post.save()
#
#        self.assertTrue(self.page.have_posts())
#
#
#class ModelPostTest(TestCase):
#
#    def setUp(self):
#
#        self.lang = Language(language='Czech', country_code='CZ')
#        self.lang.save()
#        self.menu = Menu(menu_name='menu1', lang=self.lang)
#        self.menu.save()
#        self.menuitem = MenuItem(menu=self.menu, menuitem_name='page1', url='homepage')
#        self.menuitem.save()
#        self.page = Page(link=self.menuitem, title='homepage', content='awesome homepage')
#        self.page.save()
#        self.post = Post(page=self.page, title='My first post', content='Nice text here', active=True)
#        self.post.save()
#
#        self.tz = get_current_timezone()
#
#    def test_unicode(self):
#
#        self.assertEqual(self.post.__unicode__(), self.post.title)
#
#    def test_post_is_visible(self):
#
#        self.assertTrue(self.post.is_visible(datetime(2012, 3, 5)))
#        self.assertTrue(self.post.is_visible(datetime(2014, 4, 5)))
#
#    def test_post_visible_from(self):
#
#        self.post.visible_from = make_aware(datetime(2013, 3, 17), self.tz)
#        self.post.save()
#
#        self.assertTrue(self.post.is_visible(datetime(2013, 3, 18)))
#        self.assertFalse(self.post.is_visible(datetime(203, 3, 16)))
#
#    def test_post_visible_to(self):
#
#        self.post.visible_to = make_aware(datetime(2013, 3, 17), self.tz)
#        self.post.save()
#
#        self.assertTrue(self.post.is_visible(datetime(2013, 3, 17)))
#        self.assertTrue(self.post.is_visible(datetime(2013, 3, 16)))
#        self.assertFalse(self.post.is_visible(datetime(2013, 3, 18)))
#
#    def test_post_visible_from_to(self):
#
#        self.post.visible_from = make_aware(datetime(2013, 3, 15), self.tz)
#        self.post.visible_to = make_aware(datetime(2013, 3, 20), self.tz)
#        self.post.save()
#
#        self.assertTrue(self.post.is_visible(datetime(2013, 3, 15)))
#        self.assertFalse(self.post.is_visible(datetime(2013, 3, 14)))
#        self.assertFalse(self.post.is_visible(datetime(2013, 3, 21)))
#        self.assertTrue(self.post.is_visible(datetime(2013, 3, 20)))
#
#
#class ModelCommentTest(TestCase):
#
#    'nothing to test here yet'
#
#    pass
#
#
#class ViewUrlTest(TestCase):
#
#    def test_404(self):
#
#        with self.assertRaises(Http404):
#
#            parse_url('endd/asFDSAf3~da3')
#
#    def test_language(self):
#
#        self.assertEqual(parse_url('en/'), {'page': None, 'post': None, 'page_num': None, 'country_code': 'en'})
#
#    def test_page(self):
#
#        self.assertEqual(parse_url('mypage'), {'page': 'mypage', 'post': None, 'page_num': None, 'country_code': None})
#
#    def test_post(self):
#
#        self.assertEqual(parse_url('/~mypost'), {'page': None, 'post': 'mypost', 'page_num': None, 'country_code': None})
#
#    def test_page_num(self):
#
#        self.assertEqual(parse_url('~0'), {'page': None, 'post': None, 'page_num': '0', 'country_code': None})
#
#    def test_all(self):
#
#        url = 'en/my-homepage~5/~post-on-5th-page-of-homepage'
#
#        result = {'country_code': 'en', 'page': 'my-homepage', 'page_num': '5', 'post': 'post-on-5th-page-of-homepage'}
#
#        self.assertEqual(parse_url(url), result)
