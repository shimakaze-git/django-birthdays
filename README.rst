====================
django-jp-birthdays
====================

.. image:: https://img.shields.io/github/languages/repo-size/shimakaze-git/django-jp-birthday
    :target: https://img.shields.io/github/languages/repo-size/shimakaze-git/django-jp-birthday

.. image:: https://img.shields.io/github/languages/code-size/shimakaze-git/django-jp-birthday
    :target: https://img.shields.io/github/languages/code-size/shimakaze-git/django-jp-birthday

.. image:: https://codecov.io/gh/shimakaze-git/django-jp-birthday/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shimakaze-git/django-jp-birthday

.. image:: https://img.shields.io/github/license/shimakaze-git/django-jp-birthday.svg
    :target: https://pypi.python.org/pypi/django-jp-birthday/

django-jp-birthday is a helper library to work with birthdays and ages in models.

Authored by `shimakaze_soft <https://github.com/shimakaze-git>`_,  and some great

`contributors <https://github.com/shimakaze-git/django-jp-birthday/contributors>`_.

Installation
------------

.. code-block:: bash

    python setup.py install

Usage
-----

.. code-block:: python

    from jp_birthday.models import BirthdayModel

    class ModelsTest(BirthdayModel):

        class Meta:
            app_label = 'jp_birthday'
            ordering = ('pk',)

Get all user profiles within the next 30 days:

.. code-block:: python

    ModelsTest.objects.get_upcoming_birthdays()

Get all user profiles which have their birthday today:

.. code-block:: python

    ModelsTest.objects.get_birthdays()

Or order the user profiles according to their birthday:

.. code-block:: python

    ModelsTest.objects.order_by_birthday()

Docs
-------

django-jp-birthday `docs`_

.. _docs: https://github.com/shimakaze-git/django-jp-birthday#usage


License
-------

``django-jp-birthday`` is released under the MIT license.

.. image:: https://img.shields.io/pypi/shimakaze-git/django-jp-birthday.svg
    :target: https://pypi.python.org/pypi/django-jp-birthday/
