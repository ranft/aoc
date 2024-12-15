import sys
from typing import NamedTuple

class Record(NamedTuple):
    lines: list[str]

def parse(lines):
    return Record(lines=list(map(lambda x: x.strip(), lines)))


def part1(record: Record):
    pass


def part2(record: Record):
    pass


def main():
    record=parse(sys.stdin)
    print(record)
    part1(record)
    part2(record)


if __name__ == "__main__":
    main()
