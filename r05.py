import sys
from typing import NamedTuple
from collections import defaultdict

class Pages(NamedTuple):
    rules: list[tuple[int, int]]
    pages: list[list[int]]


def parse_input(lines) -> Pages:
    rules = []
    pages = []

    for line in map(lambda x: x.strip(), lines):
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            pages.append(list(map(int, line.split(","))))
    return Pages(rules=rules, pages=pages)


def order_ruleset_from_rule_list(rules: list[tuple[int, int]]) -> dict[int, list[int]]:
    result = defaultdict(list)
    for first, second in rules:
        result[first].append(second)
    return result


def passes_ordering_rule(pages: list[int], rules: dict[int, list[int]]) -> tuple[bool, list[int]]:
    result = True
    ordered = list(pages)
    for first_index in range(len(pages)-1):
        first_number = ordered[first_index]
        for second_index in range(first_index+1, len(pages)):
            second_number = ordered[second_index]
            if order_rule := rules.get(second_number):
                if first_number in order_rule:
                    result = False
                    ordered[first_index] = second_number
                    ordered[second_index] = first_number
                    first_number, second_number = second_number, first_number
    return result, ordered


def part1(pages: Pages):
    ors = order_ruleset_from_rule_list(pages.rules)
    total = 0
    for page in (page for page in pages.pages if passes_ordering_rule(page, ors)[0]):
        mid = page[len(page)//2]
        total += mid
    print(total)


def part2(pages: Pages):
    ors = order_ruleset_from_rule_list(pages.rules)
    total = 0
    for page in pages.pages:
        ok, reordered = passes_ordering_rule(page, ors)
        print(page, ok, reordered)
        if not ok:
            mid = reordered[len(reordered)//2]
            print(mid)
            total += mid
    print(total)


def main():
    pages = parse_input(sys.stdin)
    print(pages)
    part1(pages)
    part2(pages)


if __name__ == "__main__":
    main()
