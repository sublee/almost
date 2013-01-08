# -*- coding: utf-8 -*-
from almost import almost


def test_repeating_decimal():
    assert almost(1 / 3.) == 0.333
    assert almost(1 / 6.) == 0.167
    assert almost(3227 / 555., precision=6) == 5.814414


def test_irrational_number():
    import math
    assert almost(math.pi) == 3.142
    assert almost(math.sqrt(2)) == 1.414


def test_le_ge():
    assert almost(1 / 3.) <= 0.333
    assert almost(1 / 3.) >= 0.333
    assert almost(1 / 6.) <= 0.167
    assert almost(1 / 6.) >= 0.167
    assert almost(3227 / 555., precision=6) <= 5.814414
    assert almost(3227 / 555., precision=6) >= 5.814414


def test_lt_gt():
    assert not almost(1 / 3.) < 0.333
    assert not almost(1 / 3.) > 0.333
    assert not almost(1 / 6.) < 0.167
    assert not almost(1 / 6.) > 0.167
    assert not almost(3227 / 555., precision=6) < 5.814414
    assert not almost(3227 / 555., precision=6) > 5.814414


def test_ne():
    assert not (almost(1 / 3.) != 0.333)
    assert not (almost(1 / 6.) != 0.167)
    assert not (almost(3227 / 555., precision=6) != 5.814414)


def test_pm_1():
    assert almost(1.234) == 1.233
    assert almost(1.234) == 1.235


def test_str():
    assert almost('Hello') == 'Hello'
    assert almost('Hello') != 'World'


def test_list():
    import math
    assert almost([math.pi, math.sqrt(2)]) == [3.142, 1.414]
    assert almost([math.pi, 'abc', math.sqrt(2)]) == [3.142, 'abc', 1.414]
    assert almost([math.pi, 'abc', math.sqrt(2)]) != [3.142, 'def', 1.414]


def test_dict():
    import math
    assert almost({'pi': math.pi, 'sqrt(2)': math.sqrt(2)}) == \
           {'pi': 3.142, 'sqrt(2)': 1.414}
    assert almost({'pi': math.pi, 'text': 'abc', 'sqrt(2)': math.sqrt(2)}) == \
           {'pi': 3.142, 'text': 'abc', 'sqrt(2)': 1.414}
    assert almost({'pi': math.pi, 'text': 'abc', 'sqrt(2)': math.sqrt(2)}) != \
           {'pi': 3.142, 'text': 'def', 'sqrt(2)': 1.414}


def test_gen():
    import math
    assert almost(math.sqrt(x) for x in xrange(2, 5)) == [1.414, 1.732, 2]


def test_lt_gt_list():
    import math
    assert almost([math.pi, math.sqrt(2)]) < [3.142, 1.414, 1]
    assert not (almost([math.pi, math.sqrt(2)]) > [3.142, 1.414, 1])
    assert almost([math.pi, math.sqrt(2)]) > [3.142, 1.314, 1]
    assert not (almost([math.pi, math.sqrt(2)]) < [3.142, 1.314, 1])
