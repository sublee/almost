# -*- coding: utf-8 -*-
"""
    almost
    ~~~~~~

    A helper to compare two numbers generously.

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

    :copyright: (c) 2013 by Heungsub Lee
    :license: BSD, see LICENSE for more details.
"""
try:
    from numbers import Number
except ImportError:
    # for Python 2.5
    Number = (int, float, long)
import operator
import re
import sys
from types import GeneratorType


__version__  = '0.1.1'


#: A wild card pattern in Regex.
WILDCARD = '.*'
#: The ``_sre.SRE_Pattern`` class to check normal value types.
SRE_Pattern = type(re.compile(''))
#: ``(str, unicode)`` in Python 2, ``str`` in Python 3.
String = (str, unicode) if sys.version_info[0] < 3 else str


class NormalNumber(int):
    
    pass


class Approximate(object):

    def __init__(self, value, precision=3, ellipsis='...'):
        self.value = value
        self.precision = precision
        self.ellipsis = ellipsis

    @property
    def normal(self):
        return self.normalize(self.value)

    def normalize(self, value):
        if isinstance(value, NormalNumber):
            return value
        elif isinstance(value, Number):
            try:
                fmt = '%.{0}f'.format(self.precision)
            except AttributeError:  # for Python 2.5
                fmt = '%%.%df' % self.precision
            return NormalNumber((fmt % value).replace('.', ''))
        elif isinstance(value, String):
            return re.compile(value.replace(self.ellipsis, WILDCARD))
        try:
            # detect if the valueue is iterable
            iter(value)
        except TypeError:
            pass
        else:
            if isinstance(value, dict):
                values = {}
                for key, val in value.items():
                    values[key] = self.normalize(val)
                return values
            else:
                return list(map(self.normalize, value))
        return value

    def almost_equals(self, value1, value2):
        normal1 = self.normalize(value1)
        normal2 = self.normalize(value2)
        #assert type(normal1) is type(normal2)
        if isinstance(normal1, Number):
            try:
                return abs(normal1 - normal2) <= 1
            except TypeError:
                return False
        elif isinstance(normal1, SRE_Pattern):
            return (normal1.match(normal2.pattern) or
                    normal2.match(normal1.pattern)) is not None
        elif isinstance(normal1, dict):
            if len(normal1) != len(normal2):
                return False
            return all(self.almost_equals(normal1[key], normal2[key])
                       for key in normal1.keys())
        elif isinstance(normal1, list):
            if len(normal1) != len(normal2):
                return False
            return all(self.almost_equals(*args)
                       for args in zip(normal1, normal2))
        return normal1 == normal2

    def __eq__(self, other):
        return self.almost_equals(self.value, other)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.normalize(self.value) < self.normalize(other)

    def __gt__(self, other):
        return self.normalize(self.value) > self.normalize(other)

    def __le__(self, other):
        return self.normalize(self.value) <= self.normalize(other)

    def __ge__(self, other):
        return self.normalize(self.value) >= self.normalize(other)

    def __contains__(self, other):
        normal_value = self.normalize(self.value)
        normal_other = self.normalize(other)
        assert type(normal_value) is type(normal_other)
        assert type(normal_value) is SRE_Pattern
        if (normal_value.search(normal_other.pattern) or
            normal_other.search(normal_value.pattern)):
            return True
        return (WILDCARD in normal_value.pattern or
                WILDCARD in normal_other.pattern)

    def __repr__(self):
        return 'almost(' + repr(self.value) + ')'


#: An alias of :class:`Approximate`.
almost = Approximate
