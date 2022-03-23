def solve(s):
    d = dict()
    n = len(s)
    for i in range(0, n):
        c = s[i]
        if c not in d:
            d.__setitem__(c, [])
        d[c].append(i)
    i = 0
    while i < n:
        c = s[i]
        d[c].pop(0)
        if len(d[c]) == 0:
            ans = s[i:]
            print(ans)
            return
        i += 1
    return


test = int(input())
for te in range(0, test):
    s = input()
    solve(s)