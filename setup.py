#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    "TurboGears2",
    "Beaker",
    "Pillow",
    "pdf2image",
]

setup(
    name="icaactivate",
    version="0.1",
    description="",
    author="Patrick Rauscher",
    author_email="prauscher@prauscher.de",
    url="",
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'wikir': [
        'templates/*/*',
        'public/*/*'
    ]},
    entry_points={
        'paste.app_factory': [
            'main = icaactivate.config.application:make_app'
        ]
    },
)
