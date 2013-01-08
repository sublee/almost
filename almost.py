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
__version__  = '0.1.dev'


class Almost(object):

    def __init__(self, val, precision=3):
        if isinstance(val, list):
            flatten = []
            for item in val:
                if isinstance(item, dict):
                    item = tuple(item.itervalues())
                if isinstance(item, tuple):
                    for rating in item:
                        flatten.append(tuple(rating))
            self.val = flatten
        else:
            self.val = val
        self.precision = precision

    def normalize(self, num):
        try:
            fmt = '%.{0}f'.format(self.precision)
        except AttributeError:  # for Python 2.5
            fmt = '%%.%df' % self.precision
        return int((fmt % num).replace('.', ''))

    def __eq__(self, other):
        if round(self.val, self.precision) == round(other, self.precision):
            return True
        return abs(self.normalize(self.val) - self.normalize(other)) <= 1

    def __ne__(self, other):
        if round(self.val, self.precision) != round(other, self.precision):
            return True
        return abs(self.normalize(self.val) - self.normalize(other)) > 1

    def __lt__(self, other):
        if round(self.val, self.precision) < round(other, self.precision):
            return True
        return self.normalize(self.val) < self.normalize(other)

    def __gt__(self, other):
        if round(self.val, self.precision) > round(other, self.precision):
            return True
        return self.normalize(self.val) > self.normalize(other)

    def __le__(self, other):
        if round(self.val, self.precision) <= round(other, self.precision):
            return True
        return self.normalize(self.val) <= self.normalize(other)

    def __ge__(self, other):
        if round(self.val, self.precision) >= round(other, self.precision):
            return True
        return self.normalize(self.val) >= self.normalize(other)

    def __repr__(self):
        return repr(self.val)


#: An alias.
almost = Almost
