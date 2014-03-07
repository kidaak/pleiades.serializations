#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pleiades.serializations',
    version='0.1.0',
    description='a new approach to serializing Pleiades content in multiple formats',
    long_description=readme + '\n\n' + history,
    author='Tom Elliott',
    author_email='tom.elliott@nyu.edu',
    url='https://github.com/paregorios/pleiades.serializations',
    packages=[
        'pleiades.serializations',
    ],
    package_dir={'pleiades.serializations': 'pleiades.serializations'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='pleiades.serializations',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)