#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, gneiss development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------
import re
import ast
from glob import glob

from setuptools import find_packages, setup


classes = """
    Development Status :: 5 - Production/Stable
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('Vanilla regression methods for microbiome '
               'differential abundance analysis')

long_description = description

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('songbird/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    version = str(ast.literal_eval(hit))

setup(name='songbird',
      version=version,
      description=description,
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="gneiss development team",
      author_email="jamietmorton@gmail.com",
      maintainer="gneiss development team",
      maintainer_email="jamietmorton@gmail.com",
      packages=find_packages(),
      scripts=glob('scripts/songbird'),
      setup_requires=['numpy >= 1.9.2'],
      install_requires=[
          'numpy >= 1.9.2',
          'pandas >= 0.18.0,<1',
          'scipy >= 0.15.1',
          'nose >= 1.3.7',
          'patsy',
          'scikit-bio>=0.5.1',
          'biom-format',
          'tqdm',
          'tensorflow>=1.15,<2'
      ],
      classifiers=classifiers,
      license='BSD-3-Clause',
      url="https://github.com/mortonjt/songbird",
      entry_points={
          'qiime2.plugins': ['q2-songbird=songbird.q2.plugin_setup:plugin']
      },
      package_data={'songbird': ['citations.bib']},
      zip_safe=False)
