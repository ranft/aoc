import sys


def parse(lines):
    return [tuple(map(int, line.split())) for line in lines]


def consecutive(values):
    return zip(values, values[1:])


def partials(values):
    for i in range(len(values)):
        yield values[0:i]+values[i+1:]

def deltas(values):
    return tuple((x[1] - x[0] for x in consecutive(level)))


def part1(levels: list[tuple[int, ...]]):
    result = []
    for level in levels:
        dts = tuple((x[1] - x[0] for x in consecutive(level)))
        print(dts)
        if all(x in (-3, -2, -1) for x in dts) or all(x in (1, 2, 3) for x in dts):
            result.append((level, dts))
    return result


def part2(levels: list[tuple[int, ...]]):
    result = []
    for level in levels:
        ok = False
        for sublevel in partials(level):
            dts = tuple((x[1] - x[0] for x in consecutive(sublevel)))
            print(dts)
            if all(x in (-3, -2, -1) for x in dts) or all(x in (1, 2, 3) for x in dts):
                ok = True
        if ok:
            result.append((sublevel, dts))

    return result


def main():
    with open(sys.argv[1]) as infile:
        levels = parse(infile)
    print(levels)
    print(len(part1(levels)))
    print(len(part2(levels)))


if __name__ == "__main__":
    main()
