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
from numbers import Number
import operator
from types import GeneratorType


__version__  = '0.1.0'


class Approximate(object):

    def __init__(self, val, precision=3):
        self.val = val
        self.precision = precision

    def normalize(self, val):
        if not isinstance(val, (str, unicode)):
            try:
                return map(self.normalize, val)
            except TypeError:
                pass
        if isinstance(val, Number):
            try:
                fmt = '%.{0}f'.format(self.precision)
            except AttributeError:  # for Python 2.5
                fmt = '%%.%df' % self.precision
            return int((fmt % val).replace('.', ''))
        return val

    def almost_equals(self, val1, val2):
        try:
            return abs(self.normalize(val1) - self.normalize(val2)) <= 1
        except TypeError:
            return val1 == val2

    def __eq__(self, other):
        try:
            iter(self.val)
        except TypeError:
            return self.almost_equals(self.val, other)
        else:
            vals, others = self.val, other
            if isinstance(vals, GeneratorType):
                vals = list(vals)
            if isinstance(others, GeneratorType):
                others = list(others)
            if len(vals) > len(others):
                longer = vals
            else:
                longer = others
            if isinstance(longer, dict):
                navigator = longer.iteritems()
            else:
                navigator = enumerate(longer)
            for key, __ in navigator:
                if not self.almost_equals(vals[key], others[key]):
                    return False
            return True

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.normalize(self.val) < self.normalize(other)

    def __gt__(self, other):
        return self.normalize(self.val) > self.normalize(other)

    def __le__(self, other):
        return self.normalize(self.val) <= self.normalize(other)

    def __ge__(self, other):
        return self.normalize(self.val) >= self.normalize(other)

    def __repr__(self):
        return repr(self.val)


#: An alias of :class:`Approximate`.
almost = Approximate
