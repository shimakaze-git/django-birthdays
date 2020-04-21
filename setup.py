from setuptools import setup, find_packages
from codecs import open
from os import path
import re

package_name = "django-jp-birthday"

root_dir = path.abspath(path.dirname(__file__))


def _requires_from_file(filename):
    return open(filename).read().splitlines()

with open(path.join(root_dir, 'jp_birthday', '__init__.py')) as f:
    init_text = f.read()

    version = re.search(
        r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)

    license = re.search(
        r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)

    author = re.search(
        r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)

    author_email = re.search(
        r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)

    url = re.search(
        r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)

assert version
assert license
assert author
assert author_email
assert url


def readall(path):
    with open(path, encoding="utf-8") as fp:
        return fp.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Framework :: Django',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Natural Language :: Japanese'
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    "Topic :: Software Development :: Libraries :: Python Modules",
]

extras_require = {}

kw = {
    'name':                             package_name,
    'version':                          '0.2.7',
    'description':                      'django-jp-birthday is a helper library to work with birthdays and ages in models.',
    'long_description':                 readall('README.rst'),

    'author':                           author,
    'author_email':                     author_email,
    'license':                          license,
    'keywords':                         'python birthday django',
    'url':                              url,
    'download_url':                     'https://pypi.org/project/django-jp-birthday/',
    'classifiers':                      classifiers,
    'packages':                         find_packages(exclude=['tests*']),
    'zip_safe':                         False,
    'include_package_data':             True,

    # requires
    'install_requires':                 _requires_from_file('requirements.txt'),
    'setup_requires':                   ["pytest-runner"],
    'tests_require':                    _requires_from_file('requirements-test.txt'),
    'extras_require':                   extras_require
}


if __name__ == '__main__':
    setup(**kw)
