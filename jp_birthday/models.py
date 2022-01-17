from django.db import models

from japanera import Japanera, EraDate

# from jp_birthday.fields import BirthdayField
from .fields import BirthdayField

# from jp_birthday.managers import BirthdayManager
from .managers import JpBirthdayManager

class BaseBirthdayModel(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """

    objects = JpBirthdayManager()
    birthday = BirthdayField()

    class Meta:
        abstract = True

    def _get_wareki_birthday(self):
        birthday = self.birthday

        era_date = EraDate(
            birthday.year,
            birthday.month,
            birthday.day
        )

        wareki = era_date.strftime("%-A")
        wareki_short = era_date.strftime("%-a")
        wareki_year = int(era_date.strftime("%-o"))

        return {
            'wareki' : wareki,
            'wareki_short' : wareki_short,
            'year' : int(wareki_year),
            'month' : int(birthday.month),
            'day' : int(birthday.day),
        }

    def get_wareki_birthday(self, dict_type=False):
        wareki_birthday = self._get_wareki_birthday()
        if not dict_type:
            wareki = wareki_birthday["wareki_short"]
            year = str(wareki_birthday["year"])
            month = str(wareki_birthday["month"])
            day = str(wareki_birthday["day"])
            wareki_birthday = wareki + '-' + year + '-' + month + '-' + day
        return wareki_birthday

class BirthdayModel(BaseBirthdayModel):
    """[summary]

    Args:
        BaseBirthdayModel ([type]): [description]
    """

    # order = models.PositiveIntegerField(_("order"), editable=False, db_index=True)
    # order_field_name = "order"

    class Meta:
        abstract = True
