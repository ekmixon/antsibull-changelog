
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='antsibull-changelog',
    version='0.8.0',
    description='Changelog tool for Ansible-base and Ansible collections',
    python_requires='==3.*,>=3.6.0',
    project_urls={"documentation": "https://github.com/ansible-community/antsibull-changelog/tree/main/docs/", "repository": "https://github.com/ansible-community/antsibull-changelog"},
    author='Felix Fontein',
    author_email='felix@fontein.de',
    maintainer='Toshio Kuratomi',
    maintainer_email='a.badger@gmail.com',
    license='GPL-3.0-or-later',
    entry_points={"console_scripts": ["antsibull-changelog = antsibull_changelog.cli:main"]},
    packages=['antsibull_changelog'],
    package_dir={"": "."},
    package_data={},
    install_requires=['docutils', 'packaging', 'pyyaml', 'rstcheck==3.*,>=3.0.0', 'semantic-version'],
    extras_require={"dev": ["codecov", "flake8", "mock", "mypy", "pylint", "pyre-check", "pytest", "pytest-cov"]},
)
