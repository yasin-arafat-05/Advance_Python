import sys
data = sys.stdin.read().strip()
ans = ["+".join(sorted(data.split("+"))) if len(data)>1 else data]
print(*ans)
