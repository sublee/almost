# -*- coding: utf-8 -*-
"""
Almost
~~~~~~

A helper for approximate comparison.

::

    from almost import almost
    
    def test_repeating_decimal():
        assert almost(1 / 3.) == 0.333
        assert almost(1 / 6.) == 0.167
        assert almost(3227 / 555., precision=6) == 5.814414

    def test_irrational_number():
        import math
        assert almost(math.pi) == 3.142
        assert almost(math.sqrt(2)) == 1.414

    def test_random_text():
        import random
        def gen_text_with_prefix(prefix):
            return prefix + str(random.random())[:-5]
        assert almost(gen_text_with_prefix('@')) == '@...'

Links
`````

* `GitHub repository <http://github.com/sublee/almost>`_
* `development version
  <http://github.com/sublee/almost/zipball/master#egg=almost-dev>`_

"""
from __future__ import with_statement
import re
from setuptools import setup
from setuptools.command.test import test
import sys


# detect the current version
with open('almost.py') as f:
    version = re.search(r'__version__\s*=\s*\'(.+?)\'', f.read()).group(1)
assert version


# use pytest instead
def run_tests(self):
    pyc = re.compile(r'\.pyc|\$py\.class')
    test_file = pyc.sub('.py', __import__(self.test_suite).__file__)
    raise SystemExit(__import__('pytest').main([test_file]))
test.run_tests = run_tests


setup(
    name='almost',
    version=version,
    license='BSD',
    author='Heungsub Lee',
    author_email=re.sub('((sub).)(.*)', r'\2@\1.\3', 'sublee'),
    url='http://github.com/sublee/almost',
    description='A helper to compare two numbers generously',
    long_description=__doc__,
    platforms='any',
    py_modules=['almost'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.1',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: Jython',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Topic :: Software Development :: Testing'],
    install_requires=['distribute'],
    test_suite='almosttests',
    tests_require=['pytest'],
)
