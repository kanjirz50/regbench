#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(
    name='regbench',
    version='0.1',
    description='A tiny regular expression benchmark tool.',
    author='Kanji Takahashi',
    url='https://github.com/kanjirz50/regbench',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'regbench = regbench.cli:main',
        ],
    },
)
