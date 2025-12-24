import sys
data = sys.stdin.read().strip().split()
n, k = map(int, data)

odd_count = (n + 1) // 2

if k <= odd_count:
    print(2 * k - 1)
else:
    print(2 * (k - odd_count))


