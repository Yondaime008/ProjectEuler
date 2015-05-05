def sumDivisors(a):
	sum_a = 0
	for i in range(1,a):
		if(a%i==0):
			sum_a = sum_a + i
	return sum_a

def findAmicable(a):
	b = sumDivisors(a)
	if(isAmicable(a,b) and b<10000):
		return b
	else:
		return -1


def isAmicable(a,b):
	if(sumDivisors(a)==b and sumDivisors(b)==a and a!=b):
		return True
	else: 
		return False


sommeResultat = 0
loading = 0
for a in range(0,10001):
	print(100*a/10000,"%")
	b = findAmicable(a)
	if(b!=-1):
		sommeResultat = sommeResultat + a
print(sommeResultat)
