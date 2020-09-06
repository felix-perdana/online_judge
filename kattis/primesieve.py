sieve = {}

sieve[3] = True
sieve[5] = True
sieve[7] = True
for i in range(3, 10000001, 2):
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        sieve[i] = True
