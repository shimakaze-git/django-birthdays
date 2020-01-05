from datetime import date

from django.db import models


def _order(manager, reverse=False, case=False):
    cdoy = date.today().timetuple().tm_yday
    return cdoy


class BirthdayManager(models.Manager):
    def order_by_birthday(self, reverse=False):
        return _order(self, reverse)
