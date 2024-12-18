from aoc_2_1 import Report


def test_report():
    rep = Report([1, 2, 3, 4, 5], 5)
    assert rep.is_safe() == 1


def test_report_is_still_safe_with_one_bad_jump():
    rep = Report([1, 2, 10, 4, 7], 5)
    assert rep.is_safe() == 1


def test_with_one_bad_jump_is_still_increasing():
    rep = Report([1, 2, 10, 4, 7], 5)
    assert rep._is_increasing() == True
