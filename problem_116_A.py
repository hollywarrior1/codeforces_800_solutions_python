n = int(input())
a, b = map(int, input().split())
max_, k = b, b
for i in range(n-1):
	a, b = map(int, input().split())
	k = k-a+b
	if k>max_:
		max_ = k
print(max_)
