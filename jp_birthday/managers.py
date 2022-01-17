from datetime import date

from django.db import models
from django.db.models.query_utils import Q

from jeraconv import jeraconv

import unicodedata
import jaconv

# J2W
# # from .fields import BirthdayField


# CASE = "CASE WHEN %(bdoy)s<%(cdoy)s THEN %(bdoy)s+365 ELSE %(bdoy)s END"


# def _order(manager, reverse=False, case=False):
#     cdoy = date.today().timetuple().tm_yday
#     bdoy = manager._birthday_doy_field
#     doys = {'cdoy': cdoy, 'bdoy': bdoy}
#     if case:
#         qs = manager.extra(select={'internal_bday_order': CASE % doys})
#         order_field = 'internal_bday_order'
#     else:
#         qs = manager.all()
#         order_field = bdoy
#     if reverse:
#         return qs.order_by('-%s' % order_field)
#     return qs.order_by('%s' % order_field)


# class BirthdayManager(models.Manager):

#     @property
#     def _birthday_doy_field(self):
#         return self.model._meta.birthday_field.doy_name

#     def _doy(self, day):
#         if not day:
#             day = date.today()
#         return day.timetuple().tm_yday

#     def get_upcoming_birthdays(
#         self, days=30, after=None, include_day=True, order=True, reverse=False
#     ):
#         today = self._doy(after)
#         limit = today + days
#         q = Q(
#             **{'%s__gt%s' % (
#                 self._birthday_doy_field, 'e' if include_day else ''
#             ): today}
#         )
#         q &= Q(**{'%s__lt' % self._birthday_doy_field: limit})

#         if limit > 365:
#             limit = limit - 365
#             today = 1
#             q2 = Q(**{'%s__gte' % self._birthday_doy_field: today})
#             q2 &= Q(**{'%s__lt' % self._birthday_doy_field: limit})
#             q = q | q2

#         if order:
#             qs = _order(self, reverse, True)
#             return qs.filter(q)

#         return self.filter(q)

#     def get_birthdays(self, day=None):
#         return self.filter(**{self._birthday_doy_field: self._doy(day)})

#     def order_by_birthday(self, reverse=False):
#         return _order(self, reverse)


class JpBirthdayManager(models.Manager):
    """[summary]

    Args:
        models ([type]): [description]
    """

    j2w = jeraconv.J2W()

    def _check_language(self, string):
        l_type = ""
        for ch in string:
            name = unicodedata.name(ch)

            if "CJK UNIFIED" in name:
                l_type = "kanji"
            elif "HIRAGANA" in name:
                l_type = "hiragana"
            elif "KATAKANA" in name:
                l_type = "katakana"
            elif "LATIN" in name:
                l_type = "english"
            else:
                l_type = "none"
        return l_type

    def get_wareki_birthdays(self, wareki: str):
        """[summary]

        Args:
            wareki (str): [description]
        """

        l_type = self._check_language(wareki)

        data = None
        for key, value in self.j2w._J2W__data_dic.items():
            reading = value["reading"]

            reading_jp = reading["jp"]
            reading_en = reading["en"]

            if l_type == "kanji":
                if wareki == key:
                    data = value
            elif l_type == "katakana" or l_type == "hiragana":
                wareki = jaconv.kata2hira(wareki)
                if wareki == reading_jp:
                    data = value
                    break
            elif l_type == "english":
                if wareki == reading_en:
                    data = value
                    break
            else:
                break

        if data:
            start = data["start"]
            end = data["end"]

            start_date = str(start["year"]) + "-"
            start_date += str(start["month"]) + "-"
            start_date += str(start["day"])

            end_date = str(end["year"]) + "-"
            end_date += str(end["month"]) + "-"
            end_date += str(end["day"])

            range_birthdays = self.filter(birthday__range=[start_date, end_date])
            return range_birthdays
        return self.filter(birthday=None)

    # @property
    # def _birthday_doy_field(self):
    #     # return 20
    #     # return self.model._meta.birthday_field.doy_name

    #     print('self.model._meta', self.model._meta)
    #     print('_meta.fields', self.model._meta.fields)
    #     # print('self.model._meta.birthday_field', self.model._meta.birthday_field.doy_name)

    #     # ._meta.fields

    #     # return 10
    #     # return self.model._meta.birthday_field
    #     return self.model._meta.birthday_field.doy_name

    # def _doy(self, day):
    #     if not day:
    #         day = date.today()
    #     return day.timetuple().tm_yday

    # def get_upcoming_birthdays(self, days=30, after=None, include_day=True, order=True, reverse=False):
    #     print('days', days)
    #     print('after', after)

    #     today = self._doy(after)
    #     print('today', today)

    #     limit = today + days
    #     print('limit', limit)

    #     q = Q(**{"{}__gt{}".format(self._birthday_doy_field, "e" if include_day else ""): today})
    #     q &= Q(**{"%s__lt" % self._birthday_doy_field: limit})

    #     if limit > 365:
    #         limit = limit - 365
    #         today = 1
    #         q2 = Q(**{"%s__gte" % self._birthday_doy_field: today})
    #         q2 &= Q(**{"%s__lt" % self._birthday_doy_field: limit})
    #         q = q | q2

    #     if order:
    #         qs = _order(self, reverse, True)
    #         return qs.filter(q)

    #     return self.filter(q)

    # def get_birthdays(self, day=None):
    #     print('self._doy(day)', self._doy(day))
    #     # print('_birthday_doy_field', self._birthday_doy_field)

    #     return self.filter(**{self._birthday_doy_field: self._doy(day)})
    #     # return 1

    # #     return self.filter(**{self._birthday_doy_field: self._doy(day)})

    # # def order_by_birthday(self, reverse=False):
    # #     return _order(self, reverse)
