import time
def isAbundant(n,T):
	somme = 0
	test = False
	if(checkAbundantList(n,T)):
		test = False
		return test
	if(n%2!=0 and n%3!=0 and n<5391411025):
		test = False
		return test
	if(n%2!=0 and n<945):
		test = False
		return test	


	for i in range(1,n):
		if(n%i==0):
			somme = somme + i
			if(somme>n):
				test = True
				break
	return test

def canBeSumOfTwoAbundants(n,T):
	Test = False
	if(n>46 and n%2==0):
		return True
	for i in range(1,n):
		if(isAbundant(i,T) and isAbundant(n-i,T)):
			Test = True
			break
	return Test

def checkAbundantList(n, T):
	test = False
	for i in T:
		if(n%i==0):
			test = True
			break
	return test



			

# We ommit integers above 20161  since they can 
# surely be written as sum of two abundant numbers

tic = time.clock()
T = []
#Building an array of abundant numbers to ease our search, since multiples are definitly not abundant
for i in range(1,50):
	if(isAbundant(i,T)):
		T.append(i)
print(T)
Resultat = 0
for n in range(1,20161):
	print(n*100/20161)
	if(not canBeSumOfTwoAbundants(n,T)):
		Resultat = Resultat + n
toc = time.clock()
print("Result found :",Resultat ," in ",(toc - tic)," s")

