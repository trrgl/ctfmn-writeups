sum = 0

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 1337):
    if isPrime(i):
        sum += i

print('HZU18{' + str(sum) + '}')

# OUTPUT : HZU18{133386}