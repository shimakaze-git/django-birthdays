from django.db import models

from birthday import BirthdayField, BirthdayManager

from jp_birthday.models import BirthdayModel

from jp_birthday.fields import BirthdayField as BirthdayFieldHoge
from jp_birthday.managers import JpBirthdayManager


# class TestModel(models.Model):
#     __test__ = False

#     birthday = BirthdayField()
#     objects = BirthdayManager()

#     class Meta:
#         ordering = ("pk",)


# class TestHogeModel(BirthdayModel):
class TestHogeModel(models.Model):
    __test__ = False

    birthday = BirthdayFieldHoge()
    objects = JpBirthdayManager()

    class Meta:
        ordering = ("pk",)


class ModelTest(BirthdayModel):
    class Meta:
        app_label = "jp_birthday"
        ordering = ("pk",)
