def isPrime(n):
    result = True
    for y in range(2,n):
        if(n%y==0):
            result= False
    return result
primes = 0
i=1
while(primes<=10001):
    if(isPrime(i)):
        primes = primes + 1
    i=i+1
print(i-1)
