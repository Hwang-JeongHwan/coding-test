n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    for j in range(1, n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 1번 노드에서 k까지의 최단거리 + k에서 x 까지의 최단거리 
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)