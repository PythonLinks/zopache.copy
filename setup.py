##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.copy package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

TESTS_REQUIRE = [
    'zope.component',
    'zope.location',
    'zope.testing',
    'zope.testrunner',
]

setup(name='zope.copy',
      version='4.1.0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      description='Pluggable object copying mechanism',
      long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
      keywords="zope3 copying cloning",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Zope3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Database',
      ],
      url='http://github.com/zopefoundation/zope.copy',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      install_requires=[
          'setuptools',
          'zope.interface',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='zope.copy.tests',
      extras_require={
          'test': TESTS_REQUIRE,
          'docs': [
              'Sphinx',
              'repoze.sphinx.autointerface',
          ],
      },
)
