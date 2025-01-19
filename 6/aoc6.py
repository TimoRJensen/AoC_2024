import enum
from functools import lru_cache
from pathlib import Path


class GuardDirection(enum.Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


class Scenario:
    def __init__(self, data: list[str]):
        self.data = data
        self.map = self.build_map()
        self._guard_postion: tuple[int, int] = self._get_guard_position()
        self._guard_direction: GuardDirection = self._get_guard_direction()
        self.finished = False

    def _get_guard_position(self) -> tuple[int, int]:
        return self._find_guard_position()[0]

    def _get_guard_direction(self) -> GuardDirection:
        return self._find_guard_position()[1]

    @lru_cache
    def _find_guard_position(self) -> tuple[int, int]:
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell in [
                    GuardDirection.UP.value,
                    GuardDirection.DOWN.value,
                    GuardDirection.LEFT.value,
                    GuardDirection.RIGHT.value,
                ]:
                    return ((x, y), GuardDirection(cell))

    @property
    def walked_locations(self) -> int:
        return sum([1 for cell in self.map.values() if cell == "X"])

    def print_map(self):
        for row in self._map_to_str():
            print(row)

    def _map_to_str(self) -> list[str]:
        map = []
        for y in range(len(self.data[0])):
            row = ""
            for x in range(len(self.data[0])):
                row += self.map[(x, y)]
            map.append(row)
        return map

    def build_map(self) -> dict[tuple[int, int], str]:
        map = {}
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                map[(x, y)] = cell
        return map

    def walk(self, steps: int = 0) -> None:
        if steps != 0:
            for _ in range(steps):
                self._step()
        else:
            while not self.finished:
                self._step()

    def _step(self) -> None:
        next_pos = self._get_guard_next_position()

        if self.map.get(next_pos) == "#":
            self._guard_direction = self._turn_right()
            next_pos = self._get_guard_next_position()

        self.map[self._guard_postion] = "X"
        self._guard_postion = next_pos
        print(f"Guards new position: {self._guard_postion}")

    def _turn_right(self) -> GuardDirection:
        if self._guard_direction == GuardDirection.UP:
            return GuardDirection.RIGHT
        elif self._guard_direction == GuardDirection.DOWN:
            return GuardDirection.LEFT
        elif self._guard_direction == GuardDirection.LEFT:
            return GuardDirection.UP
        elif self._guard_direction == GuardDirection.RIGHT:
            return GuardDirection.DOWN

    def _get_guard_next_position(self):
        if self._guard_direction == GuardDirection.UP:
            next_pos = (self._guard_postion[0], self._guard_postion[1] - 1)
        elif self._guard_direction == GuardDirection.DOWN:
            next_pos = (self._guard_postion[0], self._guard_postion[1] + 1)
        elif self._guard_direction == GuardDirection.LEFT:
            next_pos = (self._guard_postion[0] - 1, self._guard_postion[1])
        elif self._guard_direction == GuardDirection.RIGHT:
            next_pos = (self._guard_postion[0] + 1, self._guard_postion[1])
        if self.map.get(next_pos) is None:
            self.finished = True
            return self._guard_postion
        return next_pos


if __name__ == "__main__":
    data = Path("6/in.txt").read_text().splitlines()
    sec = Scenario(data)
    sec.walk()
    print(sec.walked_locations)
