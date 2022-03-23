import math


def solve(a, b):
    ans = 0
    i = 0
    j = 0
    m = len(a)  # test
    n = len(b)  # actual
    if n < m:
        print("IMPOSSIBLE")
        return
    while j < n and i < m:
        if a[i] == b[j]:
            i += 1
        j += 1
    if i < m:
        print("IMPOSSIBLE")
        return
    else:
        print(n - m)
    return


test = int(input())
for te in range(0, test):
    # m, n, q = list(map(int, input().split()))
    a = input()
    b = input()
    print("Case #" + str(te + 1) + ": ", end='')
    solve(a, b)