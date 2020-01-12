from django.test import TestCase

from jp_birthday.models import BirthdayModel


class ModelsTest(BirthdayModel):

    class Meta:
        app_label = 'jp_birthday'
        ordering = ('pk',)


class BirthdayTest(TestCase):

    @classmethod
    def setup_class(self):
        """ テストclass実行の前処理 """

        print('setup_class')

    def setUp(self):
        for birthday in ["2001-01-01", "2000-01-02", "2002-12-31"]:
            # raise Exception

            print('TestModel', ModelsTest)
            print("birthday", birthday)

    def test_default(self):
        from django.conf import settings

        print("test_default")
        print('settings', settings)

        # assert 1 == 2

    @classmethod
    def teardown_class(self):
        """ テストclass実行の後処理 """

        print('teardown_class')
