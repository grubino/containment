#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Install containment."""

from setuptools import (
    find_packages,
    setup
)


setup(
    name='containment',
    author='Za Wilgustus',
    author_email='zancas@contains.io',
    license='MIT',
    url='https://github.com/contains-io/containment.git',
    use_scm_version=True,
    packages=find_packages(exclude=['tests', 'docs']),
    install_requires=[
        'jinja2 >= 2.8, < 3',
        'rcli >= 0.3.3, < 0.4',
        'typet >= 0.3.3, < 0.4'
    ],
    setup_requires=[
        'pytest-runner',
        'rcli >= 0.3.3, < 0.4',
        'setuptools_scm'
    ],
    tests_require=[
        'pytest >= 3, < 4'
    ],
    autodetect_commands=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ]
)
