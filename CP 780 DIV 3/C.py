def solve(s):
    s.sort(reverse=True)
    n = len(s)
    if n == 1:
        if s[0] == 1:
            print("YES")
        else:
            print("NO")
        return
    if s[0] - s[1] > 1:
        print("NO")
    else:
        print("YES")
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    s = list(map(int, input().split()))
    solve(s)