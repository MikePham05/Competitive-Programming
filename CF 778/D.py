import math


MOD = 998244353


def solve(n, g, v):
    global MOD
    val = dict()
    for c in v.keys():
        val[c] = [1]

    check = [False for i in range(0, n + 1)]

    def dfs(node):
        nonlocal check
        check[node] = True
        for p in v[node]:
            if not check[p]:
                edge = str(node) + " " + str(p)
                ratio = g[edge]
                val[node].append(ratio[0])
                val[p].append(ratio[1])
                dfs(p)
        return

    for i in range(1, n + 1):
        if not check[i]:
            dfs(i)

    root = 0
    curr_max = 0
    for c in val.keys():
        p = 1
        for e in val[c]:
            p = math.lcm(p, e) % MOD
        if curr_max < p:
            root = c
            curr_max = p

    ans = 0
    check = [False for i in range(0, n + 1)]
    curr = curr_max
    l = []

    def backtrack(node):
        nonlocal ans, curr, l
        check[node] = True
        ans += curr
        old_curr = curr
        for p in adj[node]:
            if not check[p]:
                edge = str(node) + " " + str(p)
                ratio = g[edge]
                if curr % ratio[0] != 0:
                    l.append(ratio[0])
                curr = curr * ratio[1] / ratio[0]
                backtrack(p)
                curr = old_curr
        return

    backtrack(root)
    print(ans)
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    edge = dict()
    adj = dict()
    for i in range(0, n - 1):
        s = list(map(int, input().split()))
        gcd = math.gcd(s[2], s[3])
        if s[0] not in adj:
            adj.__setitem__(s[0], [])
        if s[1] not in adj:
            adj.__setitem__(s[1], [])
        adj[s[0]].append(s[1])
        adj[s[1]].append(s[0])
        edge.__setitem__(str(s[0]) + " " + str(s[1]), [int(s[2] / gcd), int(s[3] / gcd)])
        edge.__setitem__(str(s[1]) + " " + str(s[0]), [int(s[3] / gcd), int(s[2] / gcd)])
    solve(n, edge, adj)
