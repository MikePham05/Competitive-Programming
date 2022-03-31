def solve(a, n):
    # find all diag
    def diagonal(r, c):
        t = 0
        t += int(a[r][c])
        i = (r + 1) % n
        j = (c + 1) % n
        while i != r and j != c:
            t += int(a[i][j])
            i = (i + 1) % n
            j = (j + 1) % n
        return t

    d = [diagonal(0, 0)]
    md = d[0]
    for i in range(1, n):
        d.append(diagonal(0, i))
        md = max(md, d[-1])

    sum_a = 0
    for i in range(0, n):
        for j in range(0, n):
            sum_a += int(a[i][j])

    print(n - md + sum_a - md)
    return


test = int(input())
for te in range(0, test):
    space = input()
    n = int(input())
    a = []
    for i in range(0, n):
        b = input()
        a.append(b)
    solve(a, n)
