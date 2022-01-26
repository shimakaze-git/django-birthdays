django-jp-birthday
==================

.. figure:: https://img.shields.io/pypi/v/django_jp_birthday.svg
   :alt: https://pypi.python.org/pypi/django_jp_birthday

   https://pypi.python.org/pypi/django_jp_birthday

.. figure:: https://readthedocs.org/projects/django-jp-birthday/badge/?version=latest
   :alt: https://django-jp-birthday.readthedocs.io/en/latest/?version=latest

   https://django-jp-birthday.readthedocs.io/en/latest/?version=latest

.. figure:: https://pyup.io/repos/github/shimakaze-git/django_jp_birthday/
   :alt: https://pyup.io/repos/github/shimakaze-git/django_jp_birthday/shield.svg

   https://pyup.io/repos/github/shimakaze-git/django_jp_birthday/shield.svg

|https://img.shields.io/github/repo-size/shimakaze-git/django-jp-birthday|
|https://img.shields.io/github/languages/code-size/shimakaze-git/django-jp-birthday|
|https://codecov.io/gh/shimakaze-git/django-jp-birthday/branch/master/graph/badge.svg|
|https://img.shields.io/github/license/shimakaze-git/django-jp-birthday.svg|

Django model for Japanese birthday.

-  Free software: MIT license
-  Documentation: https://django-jp-birthday.readthedocs.io.

Features
========

-  TODO

Credits
=======

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

Main
====

django-jp-birthday is a helper library to work with birthdays and ages
in models.

Authored by ``shimakaze_soft <https://github.com/shimakaze-git>``\ \_,
and some great

``contributors <https://github.com/shimakaze-git/django-jp-birthday/contributors>``\ \_.

Installation
============

.. code:: bash

   $ pip install django-jp-birthday
   $ python steup.py install

Usage
=====

.. code:: python

   from jp_birthday.models import BirthdayModel

   class ModelsTest(BirthdayModel):

       class Meta:
           app_label = 'jp_birthday'
           ordering = ('pk',)

Get all user profiles within the next 30 days:

.. code:: python

   ModelsTest.objects.get_upcoming_birthdays()

Get all user profiles which have their birthday today:

.. code:: python

   ModelsTest.objects.get_birthdays()

Or order the user profiles according to their birthday:

.. code:: python

   ModelsTest.objects.order_by_birthday()

Docs
====

django-jp-birthday
```docs`` <https://github.com/shimakaze-git/django-jp-birthday#usage>`__

License
=======

``django-jp-birthday`` is released under the MIT license.

.. |https://img.shields.io/github/repo-size/shimakaze-git/django-jp-birthday| image:: https://img.shields.io/github/repo-size/shimakaze-git/django-jp-birthday
.. |https://img.shields.io/github/languages/code-size/shimakaze-git/django-jp-birthday| image:: https://img.shields.io/github/languages/code-size/shimakaze-git/django-jp-birthday
.. |https://codecov.io/gh/shimakaze-git/django-jp-birthday/branch/master/graph/badge.svg| image:: https://codecov.io/gh/shimakaze-git/django-jp-birthday/branch/master/graph/badge.svg
.. |https://img.shields.io/github/license/shimakaze-git/django-jp-birthday.svg| image:: https://img.shields.io/github/license/shimakaze-git/django-jp-birthday.svg

