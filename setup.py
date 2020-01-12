# import sys
import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def _requires_from_file(filename):
    print('filename', filename)
    return open(filename).read().splitlines()


classifiers = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
]

extras_require = {}

kw = {
    'name':                 'django-jp-birthday',
    'description':          'django-jp-birthday is a helper library to work with birthdays and ages in models.',
    'long_description':     open('README.rst').read(),

    'author':               'shimakaze-git',
    'license':              'MIT',
    # 'keywords':             'ansi terminal markup',
    'url':                  'https://github.com/shimakaze-git/django-jp-birthday',
    'classifiers':          classifiers,
    'packages':             find_packages(exclude=['tests*']),
    'zip_safe':             False,
    'include_package_data': True,

    # requires
    'install_requires':     _requires_from_file('requirements.txt'),
    'setup_requires':       ["pytest-runner"],
    'tests_require':        _requires_from_file('requirements-test.txt'),
    'extras_require':       extras_require
}


if __name__ == '__main__':
    setup(**kw)
