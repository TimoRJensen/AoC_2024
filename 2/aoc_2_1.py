from pathlib import Path


class Report:
    def __init__(self, levels: list[int], levels_print_length: int = 30):
        self._levels = levels
        self._levels_print_length = levels_print_length
        self._jumps: list[int] = self._get_jumps()
        self._evaluated_jumps: list[bool] = self._get_evaluated_jumps()
        self.incr_str = str(self._is_increasing()).ljust(5)
        self.decr_str = str(self._is_decreasing()).ljust(5)
        self.safe_str = str(self._all_jumps_are_safe()).ljust(5)
        self.levels_str = str(self._levels).ljust(self._levels_print_length)

    def is_safe(self, do_recurse: bool = True) -> int:
        """Returns 1 if the report is safe, 0 otherwise."""
        if (
            self._is_increasing() or self._is_decreasing()
        ) and self._all_jumps_are_safe():
            return 1
        elif do_recurse and self._any_mutated_report_is_safe():
            return 1
        return 0

    def _get_jumps(self) -> list[int]:
        jumps = []
        for i in range(len(self._levels) - 1):
            jumps.append(self._levels[i + 1] - self._levels[i])
        return jumps

    def _get_evaluated_jumps(self) -> list[bool]:
        return [self.is_safe_jump(jump) for jump in self._jumps]

    def _is_increasing(self):
        return self._levels == sorted(self._levels)

    def _is_decreasing(self):
        return self._levels == sorted(self._levels, reverse=True)

    def _all_jumps_are_safe(self):
        if all(self._evaluated_jumps):
            return True
        else:
            return False

    def _any_mutated_report_is_safe(self):
        for i in range(len(self._levels)):
            mutable_levels = self._levels.copy()
            mutable_levels.pop(i)
            sub_report = Report(levels=mutable_levels)
            if sub_report.is_safe(do_recurse=False):
                return True
        return False

    def __repr__(self):
        return (
            f"Report(levels={self._levels},"
            f" levels_print_length={self._levels_print_length})"
        )

    def __str__(self):
        return (
            f"Report: {self.incr_str} - {self.decr_str} - {self.safe_str} - "
            f"Levels:{self.levels_str} - Jumps:{self._jumps}"
        )

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


if __name__ == "__main__":
    main()
