#!/usr/bin/python3
""" N Queens """

import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def nQueens(n, i = 0, a = [], b = [], c = []):
    """
    Finding Possible positions of the queens on the chessboard.
    """

    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from nQueens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solveNQs(n):
    """
    Solving N Queens
    """

    arr = []
    i = 0
    for results in nQueens(n, 0):
        for r in results:
            arr.append([i, r])
            i += 1
        print(arr)
        arr = []
        i = 0


solveNQs(n)
