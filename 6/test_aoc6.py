import pytest
from aoc6 import Scenario


@pytest.fixture
def data() -> list[str]:
    return [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]


def test_count_walked_locations(data):
    sec = Scenario(data)
    sec.walk()
    assert sec.walked_locations == 41


def test_secenaio_can_print_same_map(data):
    sec = Scenario(data)
    assert sec._map_to_str() == data


def test_walking_one_step_truns_guard_pos_in_X(data):
    sec = Scenario(data)
    sec.walk(1)
    assert sec.map[(4, 6)] == "X"
