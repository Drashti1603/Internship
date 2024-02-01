tup = tuple(input('Enter elements: ').split())
print(tup)
y = list(tup)
y.sort()
print(y)
k = int(input('Enter k: '))
ans=[]
ans =y[:k] + y[-k:]
ans=tuple(ans)
print(ans)
