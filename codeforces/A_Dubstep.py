import sys 
data = sys.stdin.read().strip().split("WUB")
ans = ""
for i in data:
    if i!="":
        ans += " "+i 
print(ans.strip())