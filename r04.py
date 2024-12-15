import enum
import sys

content = [l.strip() for l in sys.stdin.readlines()]


vecs = (
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1, 1),
)

def addvec(start, delta):
    return start[0]+delta[0], start[1]+delta[1]


def get(vec):
    if vec[0] < 0:
        raise IndexError()
    if vec[1] < 0:
        raise IndexError()
    result = content[vec[1]][vec[0]]
    return result


def path(X, M, A, S):
    m = addvec(X, M)
    a = addvec(m, A)
    s = addvec(a, S)
    return X, m, a, s


def extract(X, M, A, S):
    xmas = path(X, M, A, S)

    try:
        result = ''.join(map(get, xmas))
        return result
    except IndexError:
        return None


def part1():
    count = 0
    for y in range(len(content)):
        for x in range(len(content[1])):
            for M in vecs:
                if (foo := extract((x, y), M, M, M)) == "XMAS":
                    print((x,y), M, M, M, path((x,y), M, M, M), foo)
                    count += 1

    print(count)


def checkX(start):
    try:
        a = get(addvec(start, (1, 1))) + get(start) + get(addvec(start, (-1, -1)))
        b = get(addvec(start, (-1, 1))) + get(start) + get(addvec(start, (1, -1)))
        ref = "MAS", "SAM"
        result = (a in ref) and (b in ref)
        return result
    except IndexError:
        return False


def part2():
    count = 0
    for y in range(len(content)):
        for x in range(len(content[1])):
            if checkX((x,y)):
                print((x,y))
                count += 1
    print(count)

part2()
