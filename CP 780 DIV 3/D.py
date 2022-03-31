def solve(s):
    f = 0
    n = len(s)

    d = []
    c2 = []
    curr = 0
    for c in s:
        if abs(c) == 2:
            curr += 1
        c2.append(curr)

    prev = -1
    for i in range(0, n):
        if s[i] == 0:
            if i > prev + 1:
                d.append([prev + 1, i - 1])
            prev = i
    if prev + 1 < n:
        d.append([prev + 1, n - 1])

    x = 0
    y = 0
    curr_max = 0
    for c in d:
        f = c[0]
        l = c[1]

        count = 0
        for i in range(f, l + 1):
            if s[i] < 0:
                count += 1

        if count % 2 == 0:
            cp = c2[l] - c2[f - 1] if f > 0 else c2[l]
            if c2[l] - c2[f - 1] > curr_max:
                curr_max = c2[l] - c2[f]
                x = f
                y = l
        else:  # neg
            # find left
            j = f
            while s[j] > 0:
                j += 1

            if c2[l] - c2[j] > curr_max:
                curr_max = c2[l] - c2[j]
                x = j + 1
                y = l

            # find right
            j = l
            while s[j] > 0:
                j += -1
            j += -1
            cp = c2[j] - c2[f - 1] if f > 0 else c2[j]
            if cp > curr_max:
                curr_max = cp
                x = f
                y = j

    if curr_max == 0:
        print(0, n)
        return

    print(x, n - 1 - y)
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    s = list(map(int, input().split()))
    solve(s)