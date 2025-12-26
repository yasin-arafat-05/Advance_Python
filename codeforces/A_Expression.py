import sys 
data = sys.stdin.read().strip().split()
arr = list(map(int,data))
"""
    1+2*3=7
    1*(2+3)=5
    1*2*3=6
    (1+2)*3=9 
"""
ans1 = arr[0]+arr[1]*arr[2]
ans2 = arr[0]*(arr[1]+arr[2])
ans3 = arr[0]*arr[1]*arr[2]
ans4 = (arr[0]+arr[1])*arr[2]
ans5 = arr[0]+arr[1]+arr[2]
ans = sorted([ans1,ans2,ans3,ans4,ans5])
print(ans[-1])