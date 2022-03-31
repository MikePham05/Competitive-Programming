def solve(s):
    d = 0  # num operation
    n = len(s)
    r = n # cha left
    curr = 0
    count = 0
    for c in s:
        count += 1
        if c == '(':
            curr += 1
        else:
            curr += -1
        if curr == 0:
            r += -count
            d += 1
    print(d, r)
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    s = input()
    solve(s)