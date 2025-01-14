from functools import lru_cache
import itertools
from pathlib import Path


class UpdateChecker:
    def __init__(self, rules: list[str]):
        self.rules = self._load_rules(rules)

    @lru_cache
    def check_update(self, update: str | tuple[int]) -> bool:
        if isinstance(update, str):
            upd = self._parse_updates(update)
        else:
            upd = update
        for rule in self.rules:
            i_0 = None
            i_1 = None
            if (rule[0] not in upd) or (rule[1] not in upd):
                continue
            for i, n in enumerate(upd):
                if n == rule[0]:
                    i_0 = i
                elif n == rule[1]:
                    i_1 = i
            if i_0 > i_1:
                # print(f"Rule {rule} violated by {upd}")
                # print(f"{i_0=}, {i_1=}")
                return False
        return True

    def _load_rules(self, raw_rules: list[str]) -> list[tuple[int, int]]:
        rv = []
        for line in raw_rules:
            first, second = line.split("|")
            rv.append((int(first), int(second)))
        return rv

    @lru_cache
    def _parse_updates(self, raw_update: str) -> list[int]:
        return [int(x) for x in raw_update.split(",")]

    def get_middle_number(self, update: str | tuple[int]):
        if isinstance(update, str):
            upd = self._parse_updates(update)
        else:
            upd = update
        return upd[len(upd) // 2]

    def get_sum_of_all_valid_middle_numbers(self, updates: list[str]) -> int:
        valid_updates = [u for u in updates if self.check_update(u)]
        return sum(self.get_middle_number(u) for u in valid_updates)

    @staticmethod
    def get_rules_and_updates(file: Path) -> tuple[list[str], list[str]]:
        with open(file, "r") as f:
            lines = f.readlines()
        rules = []
        updates = []
        for line in lines:
            if "|" in line:
                rules.append(line.strip())
            elif line.strip() == "":
                continue
            else:
                updates.append(line.strip())
        return rules, updates

    def reorder_update(self, update: str) -> list[int]:
        upd = self._parse_updates(update)
        permutations = itertools.permutations(upd)  # this is waaay too slow!
        for p in permutations:
            print(f"Checking permutation {p}")
            if self.check_update(p):
                return p

    def get_sum_of_all_invalid_middle_numbers(self, updates: list[str]) -> int:
        invalid_updates = [u for u in updates if not self.check_update(u)]
        reordered_updates = [self.reorder_update(u) for u in invalid_updates]
        return sum(self.get_middle_number(u) for u in reordered_updates)


if __name__ == "__main__":
    file = Path(__file__).parent / "input.txt"
    rules, updates = UpdateChecker.get_rules_and_updates(file)
    update_checker = UpdateChecker(rules)
    # print(update_checker.get_sum_of_all_valid_middle_numbers(updates))
    print(update_checker.get_sum_of_all_invalid_middle_numbers(updates))
