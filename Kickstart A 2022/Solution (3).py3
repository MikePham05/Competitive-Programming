import math


def solve(a, b):
    b += 1
    ans = 0
    for i in range(a, b):
        c = 0
        s = str(i)
        p = 1
        for t in s:
            p = p * int(t)
            c += int(t)
        if p % c == 0:
            ans += 1
    print(ans)
    return


test = int(input())
for te in range(0, test):
    a, b = list(map(int, input().split()))
    print("Case #" + str(te + 1) + ": ", end='')
    solve(a, b)