from dataclasses import dataclass
from logging import Logger, getLogger
from pathlib import Path
import re
from typing import Protocol


class MulComputer:
    def __init__(self, program: str):
        self.program = program
        self._mul_calls = []

    def run(self) -> int:
        self._find_mul_calls()
        return self._execute_mul_calls()

    def _find_mul_calls(self):
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        self._mul_calls = re.findall(pattern, self.program)

    def _execute_mul_calls(self):
        total = 0
        for call in self._mul_calls:
            nums = re.findall(r"\d{1,3}", call)
            total += int(nums[0]) * int(nums[1])
        return total


class Instruction(Protocol):
    def run(self) -> int | bool:
        pass


@dataclass
class MulCall:
    call: str
    start: int

    def run(self) -> int:
        nums = re.findall(r"\d{1,3}", self.call)
        return int(nums[0]) * int(nums[1])


@dataclass
class DoDontCall:
    call: str
    start: int

    @property
    def is_do_call(self) -> bool:
        return "t" not in self.call

    def run(self) -> bool:
        return self.is_do_call


class MulComputer2:
    def __init__(self, program: str):
        self.program = program
        self._mul_calls: list[MulCall] = []
        self._callable_mul_calls: list[MulCall] = []
        self._do_dont_calls: list[DoDontCall] = []
        self._all_calls: list[Instruction] = []
        self._logger: Logger = getLogger(__name__)

    def run(self) -> int:
        self._find_mul_calls()
        self._find_do_and_dont()
        self._sort_all_calls()
        return self._execute_all_calls()

    def _find_mul_calls(self):
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        self._mul_calls = [
            MulCall(call=match.group(), start=match.start())
            for match in re.finditer(pattern, self.program)
        ]

    def _find_do_and_dont(self):
        do_pattern = r"do\(\)|don't\(\)"
        self._do_dont_calls = [
            DoDontCall(call=match.group(), start=match.start())
            for match in re.finditer(do_pattern, self.program)
        ]

    def _sort_all_calls(self):
        all_calls = self._mul_calls + self._do_dont_calls
        all_calls.sort(key=lambda x: x.start)
        self._all_calls = all_calls

    def _execute_all_calls(self):
        total = 0
        do = True
        for call in self._all_calls:
            rv = call.run()
            if isinstance(rv, bool):
                do = rv
                self._logger.info(f"{call=} --> {do=}")
            elif isinstance(rv, int) and do:
                total += rv
                self._logger.info(f"{call=} --> {total=}")
        return total


if __name__ == "__main__":
    input_file = Path("./3/input")
    program = input_file.read_text()
    computer = MulComputer2(program)
    print(computer.run())
