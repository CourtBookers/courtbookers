# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='courtbookers',
    version=__import__('courtbookers').__version__,
    author='Stefan Paychère',
    author_email='stefan@pistache-soft.ch',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/CourtBookers/courtbookers',
    license='Closed',
    description='CourtBookers, bookings for sport installations',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=install_requires,
)
