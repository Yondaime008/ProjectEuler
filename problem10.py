def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

somme = 0
for i in range(1,2000001):
	if(is_prime(i)):
		somme = somme + i
print(somme)
		