import os
from setuptools import find_packages, setup


def long_desc(root_path):
    FILES = ["README.md", "CHANGES.md"]
    for filename in FILES:
        filepath = os.path.realpath(os.path.join(root_path, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode="r", encoding="utf-8") as f:
                yield f.read()


HERE = os.path.abspath(os.path.dirname(__file__))
long_description = "\n\n".join(long_desc(HERE))

install_requires = ["jeraconv", "jaconv"]


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Framework :: Django",
    "Framework :: Django :: 2.2",
    "Framework :: Django :: 3.1",
    "Framework :: Django :: 3.2",
    "Framework :: Django :: 4.0",
]

package_data = {}


setup(
    name="django-jp-birthday",
    version="0.0.1",
    description="Django model for Japanese birthday.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shimakaze-git/django-jp-birthday",
    author="shimakaze-git",
    author_email="shimakaze.soft+github@googlemail.com",
    maintainer="shimakaze-git",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    classifiers=classifiers,
    keywords="birthday era",
    install_requires=install_requires,
    package_data=package_data,
    zip_safe=False,
)
