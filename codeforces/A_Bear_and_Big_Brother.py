import sys 
data = sys.stdin.read().strip().split()
a = int(data[0]);b=int(data[1])
ans = 0 
for i in range(100000):
    if a>b:
        ans = i 
        break
    a *=3
    b *=2 
print(ans)
        
