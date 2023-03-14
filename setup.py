# -*- coding: utf-8 -*-

"""
Provides setup.
"""
import os

from setuptools import find_packages, setup

# Method for retrieving the version is taken from the setup.py of pip itself:
# https://github.com/pypa/pip/blob/master/setup.py
here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="aiosysbus",
    version="replace_by_workflow",
    packages=find_packages(),
    author="cyr-ius",
    author_email="cyr-ius@ipocus.net",
    description="Provides asynchronous authentication and access to Livebox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["httpx>=0.23.1"],
    license="GPL-3",
    include_package_data=True,
    url="https://github.com/cyr-ius/aiosysbus/tree/master/aiosysbus",
    keywords=["livebox", "async"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Home Automation",
    ],
)
