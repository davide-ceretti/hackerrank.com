def solve(a):
    # 0->1 1->2 2->3 3->6 4->7 5->14
    tot = 1
    for i in xrange(a):
        if i%2 == 1:
            tot += 1
        else:
            tot *= 2
    return tot

n = int(raw_input())
for _ in xrange(0,n):
    a = int(raw_input())
    res = solve(a)
    print res
