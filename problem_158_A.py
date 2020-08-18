n, k = map(int, input().split(' '))
str1 = list(map(int, input().split(' ')))
ans = 0
for i in range(str1[k-1], str1[0]+1):
	if i>0:
		ans+=str1.count(i)
print(ans)
