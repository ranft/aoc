import sys
from typing import NamedTuple

Coordinate = tuple[int, int]
Vector = tuple[int, int]

class Map(NamedTuple):
    obstacles: set[Coordinate]
    width: int
    height: int


class Guard(NamedTuple):
    position: Coordinate
    delta: Vector


TURNS:dict[Vector, Vector] = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}


def parse_input(lines) -> tuple[Map, Guard]:
    guard_pos = None
    width = None
    obstacles = set()
    for y, line in enumerate(map(lambda x: x.strip(), lines)):
        line_width = len(line)
        if width is not None:
            assert width == line_width
        else:
            width = line_width
        for x, chr in enumerate(line):
            if chr == "#":
                obstacles.add((x, y))
            elif chr == "^":
                assert guard_pos is None
                guard_pos = (x, y)
    assert guard_pos
    return Map(obstacles=obstacles, width=width, height=y+1), Guard(position=guard_pos, delta=(0, -1))


def next_pos(current: Coordinate, delta: Vector) -> Coordinate:
    return current[0]+delta[0], current[1]+delta[1]


def step(playground: Map, guard: Guard) -> Guard|None:
    next = next_pos(guard.position, guard.delta)
    if next in playground.obstacles:
        return Guard(position=guard.position, delta=TURNS[guard.delta])
    x, y = next
    if (x<0) or (y<0):
        return None
    if (x>=playground.width) or (y>=playground.height):
        return None
    return Guard(position=next, delta=guard.delta)


def run_steps(playground: Map, guard: Guard|None):
    turn = 0
    places = set()
    while guard is not None:
        places.add(guard.position)
        turn += 1
        guard = step(playground, guard)
        print(turn, guard)
    print(places, len(places))


def main():
    playground, guard = parse_input(sys.stdin)
    run_steps(playground, guard)

if __name__ == "__main__":
    main()
