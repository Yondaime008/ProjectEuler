n=100
res=0
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
factor = factorial(n)
print(factor)
for i in str(factor):
	res = res + int(i)
print(res)

