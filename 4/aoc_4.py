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
        for row_no, line_data in enumerate(self.data):
            self.matrix[row_no] = {}
            for column, char in enumerate(line_data):
                self.matrix[row_no][column] = char
        self.load_horizontal_slots()

    def load_horizontal_slots(self):
        for row_no, line_data in self.matrix.items():
            self.horizontal_slots_per_row[row_no] = {}
            for column, char in line_data.items():
                if column + 3 < len(line_data):
                    self.horizontal_slots_per_row[row_no][column] = Slot(
                        char,
                        line_data[column + 1],
                        line_data[column + 2],
                        line_data[column + 3],
                    )

        for row_no, line_data in self.matrix.items():
            self.horizontal_slots_per_row_reversed[row_no] = {}
            for column, char in line_data.items():
                if column - 3 >= 0:
                    self.horizontal_slots_per_row_reversed[row_no][column] = Slot(
                        char,
                        line_data[column - 1],
                        line_data[column - 2],
                        line_data[column - 3],
                    )
