# -*- encoding: utf-8 -*-

from django.db import models
from django.core.files.storage import FileSystemStorage

from ..settings import FLAG_UPLOAD_DIR

IMAGES_DIR = FileSystemStorage(FLAG_UPLOAD_DIR)


class Language(models.Model):
    '''
    Stores single language with optional flag image.
    Country Code will be part of URL in lowercase.
    '''

    language = models.CharField('Language', max_length=150, unique=True)
    country_code = models.CharField('Country code', max_length=3, unique=True)
    flag = models.ImageField(storage=IMAGES_DIR, upload_to='languages', blank=True)
    default = models.BooleanField('Display as default language?', blank=True)
    active = models.BooleanField('Active', blank=True, default=True)

    def __unicode__(self):

        return self.language

    def save(self, *args, **kwargs):
        '''
        override save method to check wheter it is first language.
        and if so, check default to True.
        if not, check if some other language has default set to True.
        if not, do not allow to set it to False.
        '''

        if not self.default:

            if not Language.objects.exists():

                self.default = True

        else:

            other_default = Language.objects.filter(default=True).exclude(id=self.id)

            if other_default:

                other_default = other_default[0]
                other_default.default = False
                # call super.save on this, so we don't check all this again
                super(Language, other_default).save(*args, **kwargs)

            self.default = True

        self.country_code = self.country_code.lower()

        super(Language, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        override delete method to check if any other language has default set.
        if not, set language with lowest ID as default.
        '''

        super(Language, self).delete(*args, **kwargs)

        if not Language.objects.filter(default=True):

            new_default = Language.objects.all().order_by('id')

            if new_default:

                new_default = new_default[0]
                new_default.default = True
                new_default.save()
