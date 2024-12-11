from collections import Counter
from pathlib import Path


class Report:
    def __init__(self, levels: list[int], levels_print_length: int):
        self._levels = levels
        self._levels_print_length = levels_print_length
        self._jumps: list[int] = []
        self.incr_str = str(self._is_increasing()).ljust(5)
        self.decr_str = str(self._is_decreasing()).ljust(5)
        self.safe_str = str(self._all_jumps_are_safe()).ljust(5)
        self.levels_str = str(self._levels).ljust(self._levels_print_length)

    def is_safe(self) -> int:
        """Returns 1 if the report is safe, 0 otherwise."""
        if (
            self._is_increasing() or self._is_decreasing()
        ) and self._all_jumps_are_safe():
            return 1
        return 0

    def __repr__(self):
        return (
            f"Report(levels={self._levels},"
            f" levels_print_length={self._levels_print_length})"
        )

    def __str__(self):
        return f"Report: {self.incr_str} - {self.decr_str} - {self.safe_str} - Levels:{self.levels_str} - Jumps:{self._jumps}"

    def _is_increasing(self):
        return self._levels == sorted(self._levels)

    def _is_decreasing(self):
        return self._levels == sorted(self._levels, reverse=True)

    def _all_jumps_are_safe(self):

        for i in range(len(self._levels) - 1):
            self._jumps.append(self._levels[i + 1] - self._levels[i])

        evaluated_jumps = [self.is_safe_jump(jump) for jump in self._jumps]

        if all(evaluated_jumps):
            return True
        else:
            cnt = Counter(evaluated_jumps)
            if (cnt[False] > 2) or (cnt[False] == 1):
                return False
            elif cnt[False] == 2:
                return self._check_if_non_safe_jumps_are_adjacent()
            else:
                raise RuntimeError("This should not happen!")

    def _check_if_non_safe_jumps_are_adjacent(self):
        for i in range(len(self._jumps) - 1):
            if not self.is_safe_jump(self._jumps[i]) and not self.is_safe_jump(
                self._jumps[i + 1]
            ):
                return True
        return False

    @staticmethod
    def is_safe_jump(jump: int):
        jump = abs(jump)
        return jump <= 3 and jump > 0


def main() -> None:
    input_file = Path("2/input")
    lines: list[int] = []
    with input_file.open() as f:
        for line in f:
            lines.append(list(map(int, line.strip().split())))

    max_report_length = max(len(report) for report in lines)
    reports: list[Report] = []
    for line in lines:
        reports.append(Report(line, max_report_length * 4))

    number_of_safe_reports = sum(report.is_safe() for report in reports)
    for report in reports:
        print(report)
    print(f"{number_of_safe_reports=}")
