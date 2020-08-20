#!/usr/bin/env python3
"""Set up the repo as python packages."""
import codecs
import os
import sys

from setuptools import find_packages, setup

NAME = "flask_intro"
AUTHOR = "Faris Chugthai"
EMAIL = "farischugthai@gmail.com"
DESCRIPTION = "flask_intro"

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(ROOT_PATH, "", "README.md")

with codecs.open(README, encoding="utf-8") as f:
    LONG_DESCRIPTION = "\n" + f.read()

# Where the magic happens:
setup_args = dict(
    name=NAME,
    # version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/restructuredtext",
    # python_requires=REQUIRES_PYTHON,
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    # url=URL,
    packages=find_packages(where=".", exclude="tests"),
    # tests_require=EXTRAS['test'],
    platforms="any",
    # install_requires=REQUIRED,
    # extras_require=EXTRAS,
    test_suite="tests",
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },
    # license_files=LICENSE,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX:: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

if len(sys.argv) > 1:
    setup(**setup_args)
