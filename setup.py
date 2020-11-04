#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search('^version\s*=\s*"(.*)"', open('txt_to_excel/txt_to_excel.py').read(), re.M).group(1)

with open("docs/README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "uhh-txt-to-excel",
    packages = ["txt_to_excel"],
    entry_points = {
        "console_scripts": ['txt-to-excel = txt_to_excel.txt_to_excel:main']
    },
    version = version,
    description = "Process special txt files into an excel worksheet.",
    long_description = long_descr,
    author = "Jannis Krämer",
    author_email = "jannis@4kraemer.me",
    url = "https://github.com/Johnderate/homebrew-txt-to-excel",
    install_requires=['et_xmlfile', 'jdcal', 'openpyxl']
)