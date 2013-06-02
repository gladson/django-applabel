django-applabel
===============

Rename Django app label in admin

Instalation
-----------

Instalation is very simple over pip.

    $ pip install django-applabel

Usage:
add settings.py

    INSTALLED_APPS += ("applabel", )

edit myapp/admin.py

    from applabel import rename
    rename(myapp, "My Application")

Authors
-------
*  Ondrej Sika, <http://ondrejsika.com>, dev@ondrejsika.com

Source
------
* Documentation: <http://ondrejsika.com/docs/django-applabel>
* Python Package Index: <http://pypi.python.org/pypi/django-applabel>
* GitHub: <https://github.com/sikaondrej/django-applabel>
