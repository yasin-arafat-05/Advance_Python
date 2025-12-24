import sys 
data = sys.stdin.read().strip().split()
arr = set(data)
print(4-len(arr))