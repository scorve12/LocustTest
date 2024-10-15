q = int(input())

commands = input().strip()

a, b = 1, 1

for command in commands:
    if command == 'R':
        b = min(b + 1, q)
    elif command == 'L':
        b = max(b - 1, 1)
    elif command == 'U':
        a = max(a - 1, 1)
    elif command == 'D':
        a = min(a + 1, q)

print(a, b)