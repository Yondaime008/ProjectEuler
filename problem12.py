result = 0
i=1
number=0
while(result<500):
	result = 0
	number = number + i
	for j in range(1,number+1):
		if(number%j==0):
			result = result + 1
	i = i+1
print(number)