import sys

input = sys.stdin.buffer.readline

n, m = map(int, input().split())

INF = 10**18
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

# Read edges
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = w

# Floyd-Warshall
for k in range(n):
    dk = dist[k]

    for i in range(n):
        dik = dist[i][k]

        if dik == INF:
            continue

        di = dist[i]

        for j in range(n):
            new_dist = dik + dk[j]

            if new_dist < di[j]:
                di[j] = new_dist

# Queries
q = int(input())

ans = []

for _ in range(q):
    u, v = map(int, input().split())
    d = dist[u - 1][v - 1]

    if d == INF:
        ans.append("-1")
    else:
        ans.append(str(d))

sys.stdout.write("\n".join(ans))