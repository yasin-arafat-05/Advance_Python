import sys
data = sys.stdin.read()
ans = ["+".join(sorted(data.split("+"))) if len(data)>1 else data]
print(*ans)

