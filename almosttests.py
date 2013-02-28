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


def test_special_number():
    assert almost(float('inf')) == float('inf')
    assert almost(float('nan')) == float('nan')
    assert almost(float('inf')) != float('nan')
    assert almost(float('inf')) != 12345
    assert almost(float('nan')) != 12345
    assert almost(float('-inf')) == -float('inf')


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
    assert almost(math.sqrt(x) for x in range(2, 5)) == [1.414, 1.732, 2]


def test_lt_gt_list():
    import math
    assert almost([math.pi, math.sqrt(2)]) < [3.142, 1.414, 1]
    assert not (almost([math.pi, math.sqrt(2)]) > [3.142, 1.414, 1])
    assert almost([math.pi, math.sqrt(2)]) > [3.142, 1.314, 1]
    assert not (almost([math.pi, math.sqrt(2)]) < [3.142, 1.314, 1])


def test_recursive_list():
    import math
    assert almost([[math.pi], [math.sqrt(2)]]) == [[3.142], [1.414]]
    assert almost([[math.pi], ['abc', math.sqrt(2)]]) == \
           [[3.142], ['abc', 1.414]]
    assert almost([[math.pi, 'abc'], [math.sqrt(2)]]) != \
           [[3.142, 'def'], [1.414]]
    assert almost([[1], [2]]) <= [[1], [2]]
    assert not (almost([[1], [2]]) < [[1], [2]])
    assert almost([[1], [2]]) >= [[1], [2]]
    assert not (almost([[1], [2]]) > [[1], [2]])
    assert not (almost([[1], [2]]) != [[1], [2]])


def test_ellipsis():
    assert almost('Hello, world') == 'Hello, ...'
    assert almost('Hello, ...') == 'Hello, world'
    assert almost('..., ...') == 'Hello, world'
    assert almost('..., ...') == '..., world'
    assert almost('..., ...') == '..., ...'
    assert almost('...') == 'Hello, world'
    assert 'world' in almost('Hello, world')
    assert 'earth' not in almost('Hello, world')
    assert 'He...' in almost('Hello, world')
    assert '...ld' in almost('Hello, world')
    assert 'o, wo' in almost('Hello, world')
    assert 'world' in almost('Hello, ...')
    assert 'angel' in almost('Hello, ...')
    assert 'world' not in almost('Hello, ..')
    assert almost([['Hello, ...'], ['..., world']]) == \
           [['Hello, world'], ['Hello, world']]
    assert almost([['Hello, ...'], ['..., world']]) != \
           [['Bye, world'], ['Hello, world']]


def test_random_text():
    import random
    def gen_text_with_prefix(prefix):
        return prefix + str(random.random())[:-5]
    assert almost(gen_text_with_prefix('@')) == '@...'
