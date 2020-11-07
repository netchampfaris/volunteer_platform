# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in volunteer_platform/__init__.py
from volunteer_platform import __version__ as version

setup(
	name='volunteer_platform',
	version=version,
	description='Volunteering Management Platform',
	author='FOSS United',
	author_email='hello@fossunited.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
