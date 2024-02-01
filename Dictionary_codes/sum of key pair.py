# Python3 implementation of
def FindSum(arr):
	l = []
	for i in arr:
		l.append(i + arr[i])
	print(*l)
arr = {1: 10, 2: 20, 3: 30}
FindSum(arr)
