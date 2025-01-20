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
        self._loops_found: set[tuple[int, int]] = set()

    def finish(self) -> None:
        self.finished = True

    def _get_guard_position(self) -> tuple[int, int]:
        return self._find_guard_position()[0]

    def _get_guard_direction(self) -> GuardDirection:
        return self._find_guard_position()[1]

    @lru_cache
    def _find_guard_position(self) -> tuple[tuple[int, int], GuardDirection]:
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell in [
                    GuardDirection.UP.value,
                    GuardDirection.DOWN.value,
                    GuardDirection.LEFT.value,
                    GuardDirection.RIGHT.value,
                ]:
                    return ((x, y), GuardDirection(cell))
                else:
                    continue
        raise ValueError("No guard found in the data")

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
        next_pos, finished = self._get_guard_next_position(
            start=self._guard_postion, direction=self._guard_direction
        )
        if finished:
            self.finish()

        if self.map.get(next_pos) == "#":
            self._guard_direction = self._turn_right(self._guard_direction)
            next_pos, finished = self._get_guard_next_position(
                start=self._guard_postion, direction=self._guard_direction
            )
            if finished:
                self.finish()
        else:
            self._simulate_obstacle_to_find_loop()

        self.map[self._guard_postion] = "X"
        self._guard_postion = next_pos
        print(f"Guards new position: {self._guard_postion}")

    def _simulate_obstacle_to_find_loop(self) -> None:
        current_pos = self._guard_postion
        sim_direction = self._turn_right(self._guard_direction)
        next_pos, finished = self._get_guard_next_position(
            start=current_pos, direction=sim_direction
        )
        while True:
            if finished:
                break
            next_pos, finished = self._get_guard_next_position(
                start=next_pos, direction=sim_direction
            )
            if self.map.get(next_pos) == "#":
                sim_direction = self._turn_right(sim_direction)
            if next_pos == current_pos:
                self._loop_found()
                break

    def _loop_found(self) -> None:
        self._loops_found.add(self._guard_postion)

    def _turn_right(self, starting_direction: GuardDirection) -> GuardDirection:
        if starting_direction == GuardDirection.UP:
            return GuardDirection.RIGHT
        elif starting_direction == GuardDirection.DOWN:
            return GuardDirection.LEFT
        elif starting_direction == GuardDirection.LEFT:
            return GuardDirection.UP
        elif starting_direction == GuardDirection.RIGHT:
            return GuardDirection.DOWN
        else:
            raise ValueError("Invalid direction")

    def _get_guard_next_position(
        self, start: tuple[int, int], direction: GuardDirection
    ) -> tuple[tuple[int, int], bool]:
        if direction == GuardDirection.UP:
            next_pos = (start[0], start[1] - 1)
        elif direction == GuardDirection.DOWN:
            next_pos = (start[0], start[1] + 1)
        elif direction == GuardDirection.LEFT:
            next_pos = (start[0] - 1, start[1])
        elif direction == GuardDirection.RIGHT:
            next_pos = (start[0] + 1, start[1])
        if self.map.get(next_pos) is None:
            return self._guard_postion, True
        return next_pos, False

    def get_number_of_possible_loops(self) -> int:
        return len(self._loops_found)


if __name__ == "__main__":
    data = Path("6/in.txt").read_text().splitlines()
    sec = Scenario(data)
    sec.walk()
    print(sec.walked_locations)
