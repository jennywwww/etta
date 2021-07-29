import sys

import setuptools
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='etta',
  version='0.1.1',
  license='MIT',
  author='Weijie Wang',
  author_email='jenny.wang2000@hotmail.com',
  packages=['etta'],
  url='https://github.com/jennywwww/etta',
  project_urls={
    'Bug Tracker': 'https://github.com/jennywwww/etta/issues',
  },
  description='Wrappers for the ExoFOP-TESS PHP functions.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  include_package_data=True,
  package_data={'': ['README.md', 'LICENSE']},
  install_requires=[
    'pandas>=1.0.0',
    'requests>=2.23.0',
    'setuptools>=41.0.0'
  ],
  classifiers=[
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.0',
  ],
)
