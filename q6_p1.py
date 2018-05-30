primes = list(range(2, 101))
for i in range(2, 10): 
    primes = list(filter(lambda x: x == i or x % i, primes))
print(primes)
