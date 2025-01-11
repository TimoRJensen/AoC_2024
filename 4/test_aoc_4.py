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


def test_finder_finds_an_xmas_in_row(data):
    finder = XmasFinder(data)
    finder.load_matrix()
    assert finder.horizontal_slots_per_row[0][5].is_xmas()


def test_finder_finds_an_xmas_in_reversed_row(data):
    finder = XmasFinder(data)
    finder.load_matrix()
    pprint(finder.horizontal_slots_per_row_reversed)
    assert finder.horizontal_slots_per_row_reversed[1][5].is_xmas()
