# Use generator to generate a stream of primes
def gen_primes():
    n = 2
    while True:
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n
        n += 1

for p in gen_primes():
    print(p)
