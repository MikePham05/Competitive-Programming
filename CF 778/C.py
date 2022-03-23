import heapq
import math


def solve(s):
    n = len(s)
    s.sort(reverse=True)
    d = dict()
    total = sum(s)
    h = []
    heapq.heappush(h, -total)
    for c in s:
        curr_max = total
        while c < curr_max:
            curr_max = -heapq.heappop(h)
            if c == curr_max:
                continue
            elif c < curr_max:
                heapq.heappush(h, math.ceil(-curr_max/2))
                heapq.heappush(h, math.floor(-curr_max/2))
            else:
                print("NO")
                return
    print("YES")
    return


test = int(input())
for te in range(0, test):
    n = int(input())
    s = list(map(int, input().split()))
    solve(s)