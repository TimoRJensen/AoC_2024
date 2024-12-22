from aoc_3 import DoDontCall, MulComputer, MulComputer2


def test_aoc_3():
    program = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    computer = MulComputer(program)
    assert computer.run() == 161


def test_aoc_3_with_2_code():
    program = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    computer = MulComputer2(program)
    assert computer.run() == 161


def test_aoc_3_second_part():
    program = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    computer = MulComputer2(program)
    assert computer.run() == 48


def test_init_dont_call_sets_is_do_to_False():
    dont_call = DoDontCall("don't()", 0)
    assert dont_call.is_do_call is False
    assert dont_call.run() is False
