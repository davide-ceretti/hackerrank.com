def solve(a, b):
    vals = xrange(a,b+1)
    return max((x ^ y for x in vals for y in vals))

a = int(raw_input())
b = int(raw_input())
print solve(a, b)
