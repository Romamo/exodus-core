#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


if sys.version_info.major == 3 and sys.version_info.minor < 3:
    print("Unfortunately, your python version is not supported!\n Please upgrade at least to python 3.3!")
    sys.exit(1)

#if sys.platform == 'darwin' or sys.platform == 'win32':
#    print("Unfortunately, we do not support your platform %s" % sys.platform)
#    sys.exit(1)

install_requires = [
    'androguard==4.0.1',
    'cryptography==38.0.1',
    'dhash==1.4',
    'jellyfish==0.5.6',
    'Pillow==9.5.0',
    'requests>=2.23,<2.32',
    'six==1.15.0',
    'traitlets==4.3.2'
]

setup(
    name='exodus_core',
    version='1.3.12.7',
    description='Core functionality of εxodus',
    author='Exodus Privacy',
    author_email='contact@exodus-privacy.eu.org',
    url='https://github.com/Exodus-Privacy/exodus-core',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "test*", "tests"]),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)
