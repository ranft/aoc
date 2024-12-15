import sys
from typing import NamedTuple

class TestRecord(NamedTuple):
    result: int
    numbers: list[int]


def parse(lines) -> list[TestRecord]:
    result = []
    for line in map(lambda x: x.strip(), lines):
        res_str, rest = line.split(":")
        numbers = list(map(int, rest.split()))
        result.append(TestRecord(result=int(res_str), numbers=numbers))
    return result


def check_two_record(result: int, a:int, b: int):
    return (result == a+b) or (result == a*b)


def check_many_record(result: int, a:int, b: int, *remainder: list[int]):
    if remainder:
        new_rem = remainder[1:]
        return check_many_record(result, a+b, remainder[0], *new_rem) or check_many_record(result, a*b, remainder[0], *new_rem)
    return check_two_record(result, a, b)

def main():
    records = parse(sys.stdin)
    total = 0
    for rec in records:
        if check_many_record(rec.result, *rec.numbers):
            total += rec.result
    print(total)


if __name__ == "__main__":
    main()
