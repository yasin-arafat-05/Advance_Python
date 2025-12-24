import sys 
data = sys.stdin.read().strip().split(" ")
k = int(data[0])
n_dollars = int(data[1])
w_buy = int(data[2])
ans = sum([i*k for i in range(1,w_buy+1)]) - n_dollars
print(0 if ans<0 else ans)

