n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        if data[i] != data[j]:
            count += 1

print(count)