import sys
from typing import NamedTuple, Optional
from collections import defaultdict

class Coordinate(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Vector") -> "Coordinate":
        return Coordinate(x=self.x+other.x, y=self.y+other.y)

    def __sub__(self, other: "Coordinate|Vector") -> "Vector|Coordinate":
        if isinstance(other, Vector):
            ctor = Coordinate
        else:
            ctor = Vector
        return ctor(x=self.x-other.x, y=self.y-other.y)

class Vector(NamedTuple):
    x: int
    y: int

    def __mul__(self, n: int):
        return Vector(x=self.x*n, y=self.y*n)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(x=self.x+other.x, y=self.y+other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(x=self.x-other.x, y=self.y-other.y)


class AntennaMap(NamedTuple):
    antenas: dict[str, list[Coordinate]]
    width: int
    height: int


def parse(lines):
    y = None
    width = None
    antenas = defaultdict(list)
    for y, line in enumerate(map(lambda x: x.strip(), lines)):
        line_width = len(line)
        if width is not None:
            assert line_width == width
        else:
            width = line_width
        for x, chr in enumerate(line):
            if chr != ".":
                antenas[chr].append(Coordinate(x, y))
    assert y is not None
    assert width is not None
    return AntennaMap(antenas=dict(antenas), width=width, height=y+1)



def in_bounds(p: Coordinate, bounds: Coordinate):
    if (p.x < 0) or (p.y < 0):
        return False
    if (p.x >= bounds.x) or (p.y >= bounds.y):
        return False
    return True

def antinodes(coordinates: list[Coordinate], bounds: Optional[Coordinate]):
    for first_index in range(len(coordinates)-1):
        for second_index in range(first_index+1, len(coordinates)):
            a = coordinates[first_index]
            b = coordinates[second_index]
            delta = b-a
            if bounds is None:
                yield(b+delta)
                yield(a-delta)
            else:
                yield b
                yield a
                p = b+delta
                while in_bounds(p, bounds):
                    yield p
                    p += delta
                p = a-delta
                while in_bounds(p, bounds):
                    yield p
                    p -= delta


def part1(record: AntennaMap):
    result = set()
    poles = set()
    field = []
    bounds = Coordinate(record.width, record.height)
    for _ in range(record.height):
        field.append(['.']*record.width)
    for antennas in record.antenas.values():
        for (x, y) in antennas:
            poles.add((x,y))
    for _name, antennas in record.antenas.items():
        for p in antinodes(antennas, None):
            if in_bounds(p, bounds):
                result.add(p)
                field[p.y][p.x] = '#'
    print(len(result), result)
    for l in field:
        print("".join(l))


def part2(record: AntennaMap):
    result = set()
    poles = set()
    field = []
    for _ in range(record.height):
        field.append(['.']*record.width)
    for antennas in record.antenas.values():
        for (x, y) in antennas:
            poles.add((x,y))
    for _name, antennas in record.antenas.items():
        for (x, y) in antinodes(antennas, Coordinate(record.width, record.height)):
            result.add((x,y))
            field[y][x] = '#'
    print(len(result), result)
    for l in field:
        print("".join(l))


def main():
    record=parse(sys.stdin)
    part1(record)
    part2(record)


if __name__ == "__main__":
    main()
