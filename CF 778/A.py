def solve(s):
    ans = 0
    s.sort(reverse=True)
    ans = s[0] + s[1]
    print(ans)
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    s = list(map(int, input().split()))
    solve(s)