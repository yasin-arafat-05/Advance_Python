n = int(input())

x = input().split()
y = input().split()

levels = set(map(int, x[1:] + y[1:]))

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
