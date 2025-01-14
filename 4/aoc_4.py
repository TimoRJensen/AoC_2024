from dataclasses import dataclass
from pathlib import Path


@dataclass
class Slot:
    first: str
    second: str
    third: str
    fourth: str

    def is_xmas(self):
        return all(
            [
                self.first == "X",
                self.second == "M",
                self.third == "A",
                self.fourth == "S",
            ]
        )


class XmasFinder:
    PATTERN_HORIZONTAL = ((0, 1), (0, 2), (0, 3))
    PATTERN_HORIZONTAL_REVERSED = ((0, -1), (0, -2), (0, -3))
    PATTERN_VERTICAL = ((1, 0), (2, 0), (3, 0))
    PATTERN_VERTICAL_REVERSED = ((-1, 0), (-2, 0), (-3, 0))
    PATTERN_DIAGONAL_DOWN = ((1, 1), (2, 2), (3, 3))
    PATTERN_DIAGONAL_DOWN_REVERSED = ((-1, -1), (-2, -2), (-3, -3))
    PATTERN_DIAGONAL_UP = ((-1, 1), (-2, 2), (-3, 3))
    PATTERN_DIAGONAL_UP_REVERSED = ((1, -1), (2, -2), (3, -3))

    PATTERNS = (
        PATTERN_HORIZONTAL,
        PATTERN_HORIZONTAL_REVERSED,
        PATTERN_VERTICAL,
        PATTERN_VERTICAL_REVERSED,
        PATTERN_DIAGONAL_DOWN,
        PATTERN_DIAGONAL_DOWN_REVERSED,
        PATTERN_DIAGONAL_UP,
        PATTERN_DIAGONAL_UP_REVERSED,
    )

    def __init__(self, data):
        self.data = data
        self.chars: dict[tuple[int, int], str] = {}

    def load_matrix(self):
        for row_no, line_data in enumerate(self.data):
            for column, char in enumerate(line_data):
                self.chars[(row_no, column)] = char

    def count_pattern_matches(self) -> int:
        rv = 0
        for pattern in self.PATTERNS:
            for char in self.chars.items():
                if char[1] != "X":
                    continue
                if self.check_pattern(char, pattern):
                    rv += 1
        return rv

    def check_pattern(self, char_x_y, pattern):
        (row, column), char = char_x_y
        y_1, x_1 = pattern[0]  # offset M
        y_2, x_2 = pattern[1]  # offset A
        y_3, x_3 = pattern[2]  # offset S
        try:
            result = all(
                [
                    self.chars[(row + y_1, column + x_1)] == "M",
                    self.chars[(row + y_2, column + x_2)] == "A",
                    self.chars[(row + y_3, column + x_3)] == "S",
                ]
            )
            if result:
                print(f"Pattern found at {row}, {column}")
                print(f"{char_x_y=}, {pattern=}")
                return True
        except KeyError:
            return False


if __name__ == "__main__":
    file = Path(__file__).resolve().parent / "input.txt"
    input_data = file.read_text().splitlines()
    finder = XmasFinder(input_data)
    finder.load_matrix()
    print(finder.count_pattern_matches())
