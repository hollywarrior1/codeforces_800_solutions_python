str1 = input()
u = 0
l = 0
for i in range(len(str1)):
	if str1[i].isupper():
		u+=1
	else:
		l+=1
if u>l:
	print(str1.upper())
else:
	print(str1.lower())