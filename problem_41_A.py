str1 = input()
str2 = list(map(str, input()))
str2.reverse()
if str1 == ''.join(str2):
	print("YES")
else:
	print("NO")