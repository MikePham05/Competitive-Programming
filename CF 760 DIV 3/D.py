def solve(s, k):
    n = len(s)
    s.sort()
    ans = 0
    for i in range(0,n - k * 2):
        ans += s[i]
    for i in range(n - k * 2, n - k):
        ans += int(s[i]/s[i+k])
    print(ans)
    return


test = int(input())
for te in range(0, test):
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))
    solve(s, k)