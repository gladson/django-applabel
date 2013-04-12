#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-applabel",
    version = "1.0.1",
    url = 'http://ondrejsika.com/docs/django-applabel',
    download_url = 'https://github.com/sikaondrej/django-applabel',
    license = 'GNU LGPL v.3',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    py_modules = ["applabel"],
    #packages = find_packages(),
    install_requires = [],
    include_package_data = True,
    zip_safe = False,
)
