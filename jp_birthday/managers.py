from django.conf import settings

from django.db import models, router, connection
from django.db.models import Case, When, Value, IntegerField

# from django.db.models.query_utils import Q

from jeraconv import jeraconv

# from math import pow
from datetime import datetime, date, time, timedelta
import pytz

import unicodedata
import jaconv


class JpBirthdayQuerySet(models.QuerySet):
    def __init__(self, model=None, query=None, using=None, hints=None):
        super().__init__(model, query, using, hints)

    def order_by_ids_filter(self, ids: list):
        cases = [When(id=id, then=Value(i + 1)) for i, id in enumerate(ids)]

        birthdays = (
            self.filter(id__in=ids)
            .annotate(md_order=Case(*cases, output_field=IntegerField()))
            .order_by("md_order")
        )

        return birthdays


class JpBirthdayManager(models.Manager):
    """[summary]

    Args:
        models ([type]): [description]
    """

    j2w = jeraconv.J2W()

    def get_queryset(self):
        return JpBirthdayQuerySet(self.model, using=self._db)

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

    def get_upcoming_birthdays(
        self, days=30, after=None, include_day=True, order=True, reverse=False
    ):
        """get_upcoming_birthdays

        Args:
            days (int, optional): [description]. Defaults to 30.
            after ([type], optional): [description]. Defaults to None.
            include_day (bool, optional): [description]. Defaults to True.
            order (bool, optional): [description]. Defaults to True.
            reverse (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """

        db_route = router.db_for_read(self)
        engine = settings.DATABASES[db_route]["ENGINE"]
        db_table_name = self.model._meta.db_table

        if after:
            after = datetime.combine(after, time())
            after = pytz.timezone("Asia/Tokyo").localize(after)
        else:
            after = datetime.now()

        if not include_day:
            after += timedelta(days=1)
            days -= 1
        days = str(days)

        after = after.date()
        after_str = "'{0}'".format(after)

        sql = "select {0}.*, ".format(db_table_name)

        between_sql = "between "
        if "sqlite3" in engine:
            sql += "strftime('%m-%d', birthday) as md "

            between_sql += "strftime('%m-%d', {0}) and ".format(after_str)
            between_sql += (
                "strftime('%m-%d', date({0}, 'localtime', '+{1} day'))".format(
                    after_str, days
                )
            )

            # sql += " order by birthday asc;"
        else:
            pass

        sql += "from {0} where md ".format(db_table_name)
        sql += between_sql

        if order:
            # print("order")
            # birthdays = birthdays.order_by(*("birthday",))
            sql += " order by md asc;"

        print("sql", sql)

        cursor = connection.cursor()
        try:
            cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            ids = [dict(zip(columns, row))["id"] for row in cursor.fetchall()]
            # print("ids", ids)

            birthdays = self.get_queryset().order_by_ids_filter(ids)

            return birthdays
        finally:
            cursor.close()

        # order = False
        # print("order", order)
        # print("reverse", reverse)
        # reverse = True

        # order = True
        # reverse = True

        # if order:
        #     print("order")
        #     birthdays = birthdays.order_by(*("birthday",))

        # if reverse:
        #     print("reverse")
        #     birthdays = birthdays.reverse()

    # def get_upcoming_birthdays(
    #     self, days=30, after=None, include_day=True, order=True, reverse=False
    # ):
    #     """[summary]

    #     Args:
    #         days (int, optional): [description]. Defaults to 30.
    #         after ([type], optional): [description]. Defaults to None.
    #         include_day (bool, optional): [description]. Defaults to True.
    #         order (bool, optional): [description]. Defaults to True.
    #         reverse (bool, optional): [description]. Defaults to False.

    #     Returns:
    #         [type]: [description]
    #     """
    #     # 今後の誕生日

    #     birthdays = self.filter()
    #     birthdays_list = [b.birthday_tm_yday for b in birthdays]

    #     if after:
    #         after = datetime.combine(after, time())
    #         after = pytz.timezone("Asia/Tokyo").localize(after)
    #     else:
    #         after = datetime.now()

    #     days += 1
    #     if not include_day:
    #         after = after + timedelta(days=1)
    #         days -= 1

    #     after_list = [
    #         (after + timedelta(days=i)).date().timetuple().tm_yday for i in range(days)
    #     ]

    #     idx_list = []
    #     for a_t in after_list:
    #         if birthdays_list.count(None) == len(birthdays_list):
    #             break

    #         for _ in birthdays_list:
    #             if a_t in birthdays_list:
    #                 n = birthdays_list.index(a_t)
    #                 # print("n", n, a_t, birthdays_list[n])
    #                 birthdays_list[n] = None
    #                 idx_list.append(n)

    #     pk_list = [birthdays[idx].pk for idx in idx_list]

    #     birthdays = birthdays.filter(pk__in=pk_list)
    #     if order:
    #         birthdays = birthdays.order_by(*("birthday",))

    #     if reverse:
    #         birthdays = birthdays.reverse()
    #     return birthdays

    def get_birthdays(self, day=None):
        """[summary]

        Args:
            day ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if not day:
            day = date.today()

        birthdays = self.filter(
            birthday__month__exact=day.month,
            birthday__day__exact=day.day,
        )
        return birthdays

    def order_by_birthday(self, reverse=False):
        """[summary]

        Args:
            reverse (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """

        birthdays_ids = []
        for i in range(1, 13):
            birthdays_ids += [
                b.pk
                for b in self.filter(birthday__month__exact=i).order_by(*("birthday",))
            ]

        cases = [When(id=id, then=pos) for pos, id in enumerate(birthdays_ids)]
        order = Case(*cases)

        birthdays = self.filter(id__in=birthdays_ids).order_by(order)

        if reverse:
            birthdays = birthdays.reverse()
        return birthdays
