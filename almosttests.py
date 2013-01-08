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
