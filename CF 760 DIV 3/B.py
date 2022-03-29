def solve(s):
    n = len(s)
    if len(s) == 1:
        print(s[0] + 'a')
        return

    ans = s[0]
    c = 0
    for i in range(1, n):
        if s[i-1][1] != s[i][0]:
            ans += s[i][0]
            c = 1
        ans += s[i][1]
    if c == 0:
        ans += 'a'
    print(ans)
    return


test = int(input())
for te in range(0, test):
    k = input()
    s = input().split()
    solve(s)