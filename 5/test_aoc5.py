from aoc5 import UpdateChecker
import pytest


@pytest.fixture
def rules():
    return [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]


@pytest.fixture
def updates():
    return [
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]


def test_update_is_identified_as_valid(rules, updates):
    update_checker = UpdateChecker(rules)
    assert update_checker.check_update(updates[0])


def test_update_is_identified_as_invalid(rules, updates):
    update_checker = UpdateChecker(rules)
    assert not update_checker.check_update(updates[3])


def test_update_returns_middle_number(rules, updates):
    update_checker = UpdateChecker(rules)
    assert update_checker.get_middle_number(updates[0]) == 61


def test_get_sum_of_all_valid_middle_nummbers(rules, updates):
    update_checker = UpdateChecker(rules)
    assert update_checker.get_sum_of_all_valid_middle_numbers(updates) == 143


def test_get_middle_number_of_invalid_update(rules, updates):
    update_checker = UpdateChecker(rules)
    upd = updates[4]
    reordered_update = update_checker.reorder_update(upd)
    assert update_checker.get_middle_number(reordered_update) == 29


def test_update_3_is_invalid(rules, updates):
    update_checker = UpdateChecker(rules)
    assert not update_checker.check_update(updates[3])


def test_get_sum_of_all_invalid_updates(rules, updates):
    update_checker = UpdateChecker(rules)
    assert update_checker.get_sum_of_all_invalid_middle_numbers(updates) == 123
