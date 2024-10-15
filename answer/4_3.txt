N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

sum = 0
for i in range(1, N + 1):
    if (arr[-i] + sum) / i >= K:
        sum += arr[-i]
    else:
        break

print(i - 1)