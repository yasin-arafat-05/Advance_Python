import sys
data = sys.stdin.read().strip()
data = list(data)
data[0] = data[0].capitalize()
print("".join(data))