tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            result += i
        else:
            result -= i

    print('#{} {}'.format(t, result))