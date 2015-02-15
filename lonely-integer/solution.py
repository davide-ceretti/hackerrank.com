#!/usr/bin/py
from collections import Counter
def lonelyinteger(a):
    c = Counter(a)
    rev = {v: k for k, v in c.iteritems()}
    return rev[min(rev.iterkeys())]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
