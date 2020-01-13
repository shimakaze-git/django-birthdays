==================
django-jp-birthdays
==================

django-jp-birthday is a helper library to work with birthdays and ages in models.

Authored by `shimakaze_soft <https://github.com/shimakaze-git>`_,  and some great
`contributors <https://github.com/shimakaze-git/django-jp-birthday/contributors>`_.

.. image:: https://travis-ci.com/shimakaze-git/django-jp-birthday.svg?branch=master
   :target: https://travis-ci.com/shimakaze-git/django-jp-birthday

.. image:: https://codecov.io/gh/shimakaze-git/django-jp-birthday/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shimakaze-git/django-jp-birthday

.. image:: https://img.shields.io/github/license/bashu/django-birthday.svg
    :target: https://pypi.python.org/pypi/django-birthday/

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

Reference
-------

django-jp-birthday `docs`_

.. _docs: https://django-birthday.readthedocs.io/en/latest/usage.html

License
-------

``django-jp-birthday`` is released under the MIT license.