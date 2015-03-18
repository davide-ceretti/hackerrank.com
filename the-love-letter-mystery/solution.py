from math import fabs


def solve(string):
    """
    abc -> abb -> aba (2)
    abcba (0)
    abcd -> abcc -> abcb -> abca -> abba (4)
    cba -> bba -> aba (2)
    """
    if len(string) == 1:
        return True

    ords = [ord(each) for each in string]

    length = len(ords)

    diffs = sum([fabs(ords[i] - ords[length-1-i]) for i in xrange(length/2)])

    return int(diffs)

t = raw_input()
for _ in xrange(int(t)):
    print solve(raw_input())
