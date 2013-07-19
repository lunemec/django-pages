# -*- encoding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-pages',
    version='1.0.4',
    author=u'Lukas Nemec',
    author_email='lu.nemec@gmail.com',
    url='https://github.com/lunemec/wysiwyg',
    license='see LICENCE.txt',
    description='Simple CMS for django',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)
