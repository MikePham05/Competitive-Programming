def solve(a, b):
    if a == 0:
        print('1')
        return
    print(a + b * 2 + 1)
    return
    return


test = int(input())
for te in range(0, test):
    a, b = list(map(int, input().split()))
    solve(a, b)