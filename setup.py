#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('docs/history.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    'nose'
]

setup(
    name='pyislands',
    version='0.1.0',
    description='PyIslands contains an implementation of islands genetic algorithms.',
    long_description=readme + '\n\n' + history,
    author='Slaven Glumac',
    author_email='slaven.glumac@gmail.com',
    url='https://github.com/sglumac/pyislands',
    packages=[
        'pyislands',
    ],
    package_dir={'pyislands': 'pyislands'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pyislands',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
