# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='secretary-bot',
    version='0.1.0',
    description='Secretary Bot for Line',
    long_description=readme,
    author='Sontaya',
    author_email='sontaya.sri@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)