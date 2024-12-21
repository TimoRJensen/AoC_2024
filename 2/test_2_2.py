import pytest
from aoc_2_1 import Report


def test_report():
    rep = Report([1, 2, 3, 4, 5], 5)
    assert rep.is_safe() == 1


@pytest.mark.parametrize(
    "save_report", [[1, 3, 2, 4, 5], [7, 6, 4, 2, 1], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
)
def test_report_is_still_safe_with_one_bad_jump(save_report):
    rep = Report(save_report)
    assert rep.is_safe() == 1


@pytest.mark.parametrize("unsafe_report", [[1, 2, 7, 8, 9], [9, 7, 6, 2, 1]])
def test_report_is_unsafe(unsafe_report):
    rep = Report(unsafe_report)
    assert rep.is_safe() == 0
