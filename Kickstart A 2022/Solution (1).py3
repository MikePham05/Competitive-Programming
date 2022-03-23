import math


def solve(s):
    t = 0
    for c in s:
        t += int(c)
    ch = (9 - (t % 9)) % 9
    i = 0
    if ch == 0:
        i += 1
    n = len(s)
    while i < n and int(s[i]) <= ch:
        i += 1
    ans = s[0:i] + str(ch) + s[i:]
    print(ans)
    return


test = int(input())
for te in range(0, test):
    # m, n, q = list(map(int, input().split()))
    s = input()
    print("Case #" + str(te + 1) + ": ", end='')
    solve(s)