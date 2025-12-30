import sys 
data = sys.stdin.read().strip().split()
n = int(data[0])
s = int(data[1])
for _ in range(s):
    if n%10==0:
        n = int(n/10)
    else: 
        n -= 1
print(n)
        

