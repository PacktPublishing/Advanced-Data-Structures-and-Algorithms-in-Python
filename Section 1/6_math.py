def square_free(n):

    count = 0
    for i in range(1, n+1):
        ok = True
        for j in range(2, i):
            if i % (j*j) == 0:
                ok = False
                break
        if ok:
            count += 1

    return count

def inclusion_exclusion(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def count(k, primes_used):
        if k == len(primes):
            product = 1
            for p in primes_used:
                product *= p * p
            if len(primes_used) % 2 == 0:
                return n // product
            return -(n // product)

        return count(k + 1, primes_used) + \
               count(k + 1, primes_used + [primes[k]])

    return count(0, [])

for i in range(1, 10000):
    sf = square_free(i)
    ie = inclusion_exclusion(i)
    #print(i, sf, ie)
    # supposed to fail at some point, depending on how many primes you have
    assert sf == ie, 'i={}, sf={}, ie={}'.format(i, sf, ie)