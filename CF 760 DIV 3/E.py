def solve(b):
    n = len(b)
    a = []
    # find sum of a, sa
    sa = sum(b)
    m = int(n*(n+1)/2)
    if sa % m != 0:
        print("NO")
        return
    sa = int(sa/m)
    for i in range(0, n):
        if (sa - b[i] + b[i - 1]) % n != 0:
            print("NO")
            return
        a.append(int((sa - b[i] + b[i-1])/n))
        if a[-1] <= 0:
            print("NO")
            return
    print("YES")
    print(' '.join(list(map(str, a))))
    return


test = int(input())
for te in range(0, test):
    n = input()
    b = list(map(int, input().split()))
    solve(b)