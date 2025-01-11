from dataclasses import dataclass


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
    def __init__(self, data):
        self.data = data
        self.matrix: dict[int, dict[int, str]] = {}
        self.horizontal_slots_per_row: dict[int, dict[int, Slot]] = {}
        self.horizontal_slots_per_row_reversed: dict[int, dict[int, Slot]] = {}

    def load_matrix(self):
        for row, line in enumerate(self.data):
            self.matrix[row] = {}
            for column, char in enumerate(line):
                self.matrix[row][column] = char
        self.load_horizontal_slots()

    def load_horizontal_slots(self):
        for row, line in self.matrix.items():
            self.horizontal_slots_per_row[row] = {}
            for column, char in line.items():
                if column + 3 < len(line):
                    self.horizontal_slots_per_row[row][column] = Slot(
                        char,
                        line[column + 1],
                        line[column + 2],
                        line[column + 3],
                    )

        for row, line in self.matrix.items():
            self.horizontal_slots_per_row_reversed[row] = {}
            items = sorted(line.items(), reverse=True)
