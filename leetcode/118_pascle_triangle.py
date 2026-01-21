
def fact(n):
    ans = 1 
    print(ans,end=" ")
    for i in range(1,n):
        ans *=  (n-i)/i 
        print(int(ans),end=" ")

for i in range(1,7):
    fact(i)
    print()      