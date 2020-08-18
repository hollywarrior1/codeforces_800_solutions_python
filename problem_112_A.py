st1 = input().lower()
st2 = input().lower()
for i in range(len(st1)):
	if st1[i]<st2[i]:
		print(-1)
		break
	elif st1[i]>st2[i]:
		print(1)
		break
	if i == len(st1)-1:
		print(0)