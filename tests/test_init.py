from unittest import TestCase
# from django.test import TestCase


class InitTest(TestCase):

    @classmethod
    def setup_class(self):
        """ テストclass実行の前処理 """

        print('setup_class')

    def setUp(self):
        print('setup')

    def test_default(self):
        from django.conf import settings

        print("test_default")
        print('settings', settings)

        # assert 1 == 2

    @classmethod
    def teardown_class(self):
        """ テストclass実行の後処理 """

        print('teardown_class')
