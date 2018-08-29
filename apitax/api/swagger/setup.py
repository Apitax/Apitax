# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "apitax.ah.api"
VERSION = "2"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Apitax",
    author_email="shawn.clake@nopatience.net",
    url="",
    keywords=["Swagger", "Apitax"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['apitax.ah.api=apitax.ah.api.__main__:main']},
    long_description="""\
    The API for the frontend of Apitax
    """
)

