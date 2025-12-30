data = input().lower()
ans = [ f".{ch}" if not ch in ["a", "o", "y", "e", "u", "i"] else ""  for ch in data]
print("".join(ans))