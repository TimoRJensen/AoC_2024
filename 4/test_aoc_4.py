from pprint import pprint

import pytest
from aoc_4 import XmasFinder


@pytest.fixture()
def data():
    return [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]


def test_finder(data):
    finder = XmasFinder(data)
    finder.load_matrix()
    # pprint(finder.chars)
    assert finder.count_xmas_pattern_matches() == 18


def test_x_in_5_0(data):
    finder = XmasFinder(data)
    finder.load_matrix()
    assert finder.chars[(5, 0)] == "X"


def test_pattern_5_0(data):
    finder = XmasFinder(data)
    finder.load_matrix()
    assert (
        finder.check_xmas_pattern(((5, 0), "X"), XmasFinder.PATTERN_DIAGONAL_UP) is True
    )
