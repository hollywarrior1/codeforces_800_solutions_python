n = int(input())
arr = list(map(int, input().split(' ')))
ind1 = arr.index(max(arr))
for i in range(n-1, -1, -1):
	if arr[i]==min(arr):
		ind2 = i
		break
if ind2<ind1:
	print(ind1+(n-1-ind2)-1)
else:	
	print(ind1+(n-1-ind2))