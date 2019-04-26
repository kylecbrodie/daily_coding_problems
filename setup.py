#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

setup(
	name="daily_coding_problems",
	version="0.1.0",
	license="MIT License",
	description="Solutions to coding challenges from the daily coding problem mailing list, leetcode, and others",
	author="Kyle Brodie",
	author_email="kylecbrodie@gmail.com",
	url="https://github.com/kylecbrodie/daily_coding_problems",
	packages=find_packages("src"),
	package_dir={"": "src"},
)