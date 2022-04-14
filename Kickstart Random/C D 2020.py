import sys
sys.setrecursionlimit(50000)


def solve(n, a, b, parent):
    ans = 0
    # node start at 1
    child = [[] for i in range(0, n + 1)]  # list of all child
    for i in range(2, n + 1):
        child[parent[i]].append(i)

    # parent[i] is parent of node i in the graph
    # child[i] is all children of node i

    # check reached for DFS
    reached = [False for i in range(0, n + 1)]
    # total number of node painted if starting at node i, painted[i][0] for A, painted[i][1] for B
    painted = [[1, 1] for i in range(0, n + 1)]
    curr_path = []
    # child_a, child_b for calculating duplicate
    child_a = [[] for i in range(0, n + 1)]
    child_b = [[] for i in range(0, n + 1)]

    def DFS(node):
        nonlocal child, parent, painted, reached
        reached[node] = True  # node reached
        curr_path.append(node)  # add node to the end of current path
        # update painted node, painted[0]
        if len(curr_path) - 1 - a >= 0:  # if parent Amadea exist:
            painted[node][0] = painted[curr_path[len(curr_path) - 1 - a]][0] + 1
            child_a[curr_path[len(curr_path) - 1 - a]].append(node)
        if len(curr_path) - 1 - b >= 0:  # if parent Bilva exist
            painted[node][1] = painted[curr_path[len(curr_path) - 1 - b]][1] + 1
            child_b[curr_path[len(curr_path) - 1 - b]].append(node)
        for c in child[node]:
            if not reached[c]:  # if node has not reached
                DFS(c)
                curr_path.pop()
        return

    DFS(1)

    num_child_a = [1 for i in range(0, n + 1)]
    num_child_b = [1 for i in range(0, n + 1)]
    reached = [False for i in range(0, n + 1)]

    def DFS_A(node):
        nonlocal child, parent, painted, reached
        reached[node] = True
        for c in child_a[node]:
            if not reached[c]:
                DFS_A(c)
            num_child_a[node] += num_child_a[c]
        return

    for i in range(1, n + 1):
        if not reached[i]:
            DFS_A(i)

    # build num_child_b
    reached = [False for i in range(0, n + 1)]

    def DFS_B(node):
        nonlocal child, parent, painted, reached
        reached[node] = True
        for c in child_b[node]:
            if not reached[c]:
                DFS_B(c)
            num_child_b[node] += num_child_b[c]
        return

    for i in range(1, n + 1):
        if not reached[i]:
            DFS_B(i)

    # answer with duplicated nodes
    for i in range(1, n + 1):
        ans += (painted[i][0] + painted[i][1]) * n

    # filtering out duplicated nodes
    for i in range(1, n + 1):
        ans += -(num_child_a[i] * num_child_b[i])

    # cal final expected
    ans = ans / (n * n)
    return ans


f = open("ts2_input.txt", "r")
test = int(f.readline())

for te in range(1, test + 1):
    n, a, b = list(map(int, f.readline().split()))
    parent = [0, 0]
    if n > 1:
        parent += list(map(int, f.readline().split()))
    else:
        f.readline()
    print("Case #" + str(te) + ": " + "{:.6f}".format(solve(n, a, b, parent)))