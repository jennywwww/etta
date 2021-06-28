import sys

import setuptools
from setuptools import setup

# sys.path.insert(0, "eleanor")
# I don't really understand the line below
# from version import __version__


setup(
  name='etta',
  license='MIT',
  author='Weijie Wang',
  author_email='jenny.wang2000@hotmail.com',
  packages=['etta'],
  url='https://github.com/jennywwww/exofop-tess-api',
  description='Wrappers for the ExoFOP-TESS PHP functions.',
  include_package_data=True,
  package_data={'': ['README.md', 'LICENSE']},
  install_requires=[
    'pandas>=1.0.0',
    'requests>=2.23.0',
    'setuptools>=41.0.0'],
  classifiers=[
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.0',
  ],
)
