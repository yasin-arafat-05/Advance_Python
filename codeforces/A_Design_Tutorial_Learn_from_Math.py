import sys 
data = sys.stdin.read().strip()
val  = int(data)

if val%2==0:
    print(4,val-4)
else:
    print(9,val-9)
