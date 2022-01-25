# from django.db import models

from django.test import TestCase

# from datetime import datetime, date


from tests.models import ModelTest


class InitTest(TestCase):
    @classmethod
    def setup_class(self):
        """テストclass実行の前処理"""

        print("setup_class")

    def setUp(self):
        self.meiji = ["1905-1-1", "1905-1-2"]
        self.showa = ["1980-7-7", "1975-1-1"]
        self.heisei = ["2001-01-01", "2000-01-02", "2002-12-31"]

        self.birthdays = self.meiji + self.showa + self.heisei
        for birthday in self.birthdays:
            model_test = ModelTest(birthday=birthday)
            model_test.save()

    def test_month(self):
        model_tests = ModelTest.objects.all()
        for m in model_tests:
            month = m.birthday.month
            self.assertEqual(month, m.birthday_month)

    def test_month_day(self):
        model_tests = ModelTest.objects.all()
        for m in model_tests:
            month = str(m.birthday.month)
            day = str(m.birthday.day)

            # self.assertEqual(
            #     month + '-' + day,
            #     m.birthday_month_day
            # )

    @classmethod
    def teardown_class(self):
        """テストclass実行の後処理"""

        print("teardown_class")
