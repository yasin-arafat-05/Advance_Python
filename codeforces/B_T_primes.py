""" 
t=p^2, where p is prime
Divisors of: 1, p, p²
total = 3
"""
import sys 
import math 
data = sys.stdin.read().strip().split();idx=0
t = int(data[idx]);idx+=1

#MAX = int(math.sqrt(1e12))
MAX = 10**6 + 1
is_prime = [True]*MAX
is_prime[0] = False
is_prime[1] = False

for i in range(2,int(MAX**0.5+1)):
    if is_prime[i]:
        for j in range(i*i,MAX,i):
            is_prime[j] = False
    
        
for _ in range(t):
    val = int(data[idx])
    sqrt = int(math.sqrt(val))
    if sqrt*sqrt==val and is_prime[sqrt]:
        print("YES")
    else:
        print("NO")
    idx+=1
   
   