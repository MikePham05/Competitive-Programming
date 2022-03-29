import math


def solve(s):
    a = []
    b = []
    n = len(s)
    if n == 2:
        if s[0] == s[1]:
            print(0)
        else:
            print(max(s))
        return

    for i in range(0, n):
        c = s[i]
        if i % 2 == 0:
            a.append(c)
        else:
            b.append(c)

    a.sort()
    b.sort()
    ga = a[0]
    for i in range(1, len(a)):
        ga = math.gcd(ga, a[i])

    gb = b[0]
    for i in range(1, len(b)):
        gb = math.gcd(gb, b[i])

    ans = 0
    check = True
    for c in b:
        if math.gcd(ga, c) == ga:
            check = False
    if check:
        ans = ga

    check = True
    for c in a:
        if math.gcd(gb, c) == gb:
            check = False
    if check:
        ans = gb

    print(ans)
    return


test = int(input())
for te in range(0, test):
    k = input()
    s = list(map(int, input().split()))
    solve(s)