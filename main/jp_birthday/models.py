from django.db import models

from jp_birthday.fields import BirthdayField
from jp_birthday.managers import BirthdayManager


class BaseBirthdayModel(models.Model):

    birthday = BirthdayField()

    class Meta:
        abstract = True


class BirthdayModel(BaseBirthdayModel):

    objects = BirthdayManager()
    all_objects = models.Manager()
