import math


def solve(s):
    curr = ""
    n = len(s)
    if n < 5:
        print("POSSIBLE")
        return
    check = False

    def recurse(cur, i):
        nonlocal check
        if i == n:
            for f in range(0, n - 4):
                for l in range(f + 4, n):
                    m = int((f + l)/2)
                    k = m if (f + l) % 2 == 0 else m + 1
                    if cur[f:k] == cur[m + 1:l + 1][::-1]:
                        return
            check = True
            return
        if s[i] == '?':
            for j in range(0, 2):
                cur += str(j)
                recurse(cur, i + 1)
                cur = cur[:-1]
        else:
            cur += s[i]
            recurse(cur, i + 1)
        return

    recurse(curr, 0)
    ans = "POSSIBLE"
    if not check:
        ans = "IM" + ans
    print(ans)
    return


test = int(input())
for te in range(0, test):
    # m, n, q = list(map(int, input().split()))
    nt = input()
    s = input()
    print("Case #" + str(te + 1) + ": ", end='')
    solve(s)