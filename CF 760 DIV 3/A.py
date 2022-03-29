def solve(s):
    ans = [s[0], s[1]]
    if s[2] != s[0] + s[1]:
        ans.append(s[2])
    else:
        ans.append(s[3])
    print(ans[0], ans[1], ans[2])
    return


test = int(input())
for te in range(0, test):
    s = list(map(int, input().split()))
    solve(s)