import pytest
from aoc6 import Secenario


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
    sec = Secenario(data)
    sec.walk()
    assert sec.walked_locations == 41


def test_secenaio_can_print_same_map(data):
    sec = Secenario(data)
    assert sec._map_to_str() == data


def test_walking_one_step_truns_guard_pos_in_X(data):
    sec = Secenario(data)
    sec.walk(1)
    assert sec.map[(4, 6)] == "X"
