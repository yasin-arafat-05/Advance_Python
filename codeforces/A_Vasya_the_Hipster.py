import sys 
data = sys.stdin.read().strip().split()
a=int(data[0]);b=int(data[1])
min_val = min(a,b)
max_val = max(a,b)
print(min_val,(max_val-min_val)//2)