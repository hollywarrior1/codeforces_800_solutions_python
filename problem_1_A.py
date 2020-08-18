from math import ceil
n,m,a = map(int, input().split(' '))
ans = ceil(m/a)*ceil(n/a)
print(ans)