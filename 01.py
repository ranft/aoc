#!/usr/bin/env python3

import sys


def read_input_file(name: str):
    with open(name, encoding="ascii") as infile:
        return [tuple(map(int, l.split())) for l in infile]


def sort_column(values: list[tuple[int, ...]], col: int) -> list[int]:
    return sorted(map(lambda x: x[col], values))


def part1(values) -> int:
    return sum(
        map(
            lambda xy: abs(xy[0] - xy[1]),
            zip(*map(lambda c: sort_column(values, c), [0, 1])),
        )
    )


def part2(values):
    rights = {}
    for _, right in values:
        rights[right] = rights.get(right, 0) + 1

    result = 0
    for left, _ in values:
        result += rights.get(left, 0) * left

    return result


def main():
    values = read_input_file(sys.argv[1])

    print(part1(values))
    print(part2(values))


if __name__ == "__main__":
    main()
