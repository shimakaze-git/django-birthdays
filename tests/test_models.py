from django.db import models

from django.test import TestCase
from datetime import datetime, date


from tests.models import ModelTest


class InitTest(TestCase):
    @classmethod
    def setup_class(self):
        """テストclass実行の前処理"""

        print("setup_class")

    def setUp(self):
        self.meiji = ["1905-1-2", "1905-1-1", "1905-2-1", "1905-2-2"]
        self.showa = ["1980-7-7", "1975-1-1"]
        self.heisei = ["2000-01-02", "2001-01-01", "2002-12-31"]

        birthdays = self.meiji + self.showa + self.heisei
        for birthday in birthdays:
            model_test = ModelTest(birthday=birthday)
            model_test.save()

    def test_default(self):
        model_tests = ModelTest.objects.all()
        for m in model_tests:
            month = m.birthday.month
            day = m.birthday.day

            wareki_birthday = m.get_wareki_birthday()

            wareki_month = int(wareki_birthday.split("-")[2])
            wareki_day = int(wareki_birthday.split("-")[3])

            self.assertEqual(month, wareki_month)
            self.assertEqual(day, wareki_day)

    def test_get_wareki_birthdays(self):
        wareki_birthdays = ModelTest.objects.get_wareki_birthdays("heisei")
        for m in wareki_birthdays:
            birthday = str(m.birthday)
            self.assertTrue(birthday in self.heisei)

        wareki_birthdays = ModelTest.objects.get_wareki_birthdays("へいせい")
        for m in wareki_birthdays:
            birthday = str(m.birthday)
            self.assertTrue(birthday in self.heisei)

        wareki_birthdays = ModelTest.objects.get_wareki_birthdays("平成")
        for m in wareki_birthdays:
            birthday = str(m.birthday)
            self.assertTrue(birthday in self.heisei)

    def test_get_age(self):
        model_tests = ModelTest.objects.all()
        for m in model_tests:
            age = m.get_age()
            self.assertTrue("int" in str(type(age)))

    def test_ordering(self):
        # pks1 = [obj.pk for obj in ModelTest.objects.order_by("birthday")]
        # pks2 = [obj.pk for obj in ModelTest.objects.order_by_birthday()]

        # print("pks2", pks2)

        ModelTest.objects.order_by_birthday()
        # self.assertNotEqual(pks1, pks2)

    def test_manager(self):
        jan1 = date(year=1905, month=1, day=1)
        # jan2 = date(year=2010, month=2, day=1)

        birthdays = ModelTest.objects.get_birthdays(jan1)
        # print('birthdays')

        # for m in birthdays:
        #     print(m.birthday)

        self.assertEqual(birthdays.count(), 3)

        ModelTest.objects.get_upcoming_birthdays(30, jan1)
        # ModelTest.objects.get_upcoming_birthdays(30, jan2, False)

        # self.assertEqual(TestModel.objects.get_upcoming_birthdays(30, jan1).count(), 2)
        # self.assertEqual(TestModel.objects.get_upcoming_birthdays(30, jan1, False).count(), 1)

        # dec31 = date(year=2010, month=12, day=31)
        # self.assertEqual(TestModel.objects.get_birthdays(dec31).count(), 1)
        # self.assertEqual(TestModel.objects.get_upcoming_birthdays(30, dec31).count(), 3)

        # doys = [
        #     getattr(obj, "birthday_dayofyear_internal") for obj in TestModel.objects.get_upcoming_birthdays(30, dec31)
        # ]
        # self.assertEqual(doys, [365, 1, 2])
        # doys = [
        #     getattr(obj, "birthday_dayofyear_internal")
        #     for obj in TestModel.objects.get_upcoming_birthdays(30, dec31, reverse=True)
        # ]
        # self.assertEqual(doys, [2, 1, 365])
        # doys = [
        #     getattr(obj, "birthday_dayofyear_internal")
        #     for obj in TestModel.objects.get_upcoming_birthdays(30, dec31, order=False)
        # ]
        # self.assertEqual(doys, [1, 2, 365])

        # self.assertEqual(TestModel.objects.get_upcoming_birthdays(30, dec31, False).count(), 2)
        # self.assertTrue(TestModel.objects.get_birthdays().count() in [0, 1])

    @classmethod
    def teardown_class(self):
        """テストclass実行の後処理"""

        print("teardown_class")
