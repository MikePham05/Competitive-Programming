a, b = map(int, input().split())
s = bin(b)[2:]
t = bin(a)[2:]
if s == t:
    print("YES")
    exit(0)
for q in [t + '1', t.strip('0')]:
    for l in range(len(s) - len(q) + 1):
        r = len(s) - len(q) - l
        if '1' * l + q + '1' * r == s or '1' * l + q[::-1] + '1' * r == s:
            print("YES")
            exit(0)
print("NO")