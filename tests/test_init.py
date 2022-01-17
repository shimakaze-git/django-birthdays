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
        self.showa = ["1980-7-7"]
        self.heisei = ["2001-01-01", "2000-01-02", "2002-12-31"]

        birthdays = self.showa + self.heisei
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

    @classmethod
    def teardown_class(self):
        """テストclass実行の後処理"""

        print("teardown_class")
