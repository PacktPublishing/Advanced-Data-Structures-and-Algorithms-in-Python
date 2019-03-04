from time import clock

def eratosthenes_1(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def eratosthenes_2(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(4, n+1, 2):
        sieve[i] = False
    for i in range(3, n+1, 2):
        if sieve[i]:
            for j in range(i+i+i, n+1, i+i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def eratosthenes_3(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(4, n+1, 2):
        sieve[i] = False
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            for j in range(i*i, n+1, i+i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

import numpy as np
def eratosthenes_np(n):
    sieve = np.ones(n+1, dtype=np.bool)
    sieve[0] = sieve[1] = 0
    sieve[4::2] = 0
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i*i::i+i] = 0
    return list(np.nonzero(sieve)[0])


# tests
for i in range(2, 1000):
    e1 = eratosthenes_1(i)
    e2 = eratosthenes_2(i)
    e3 = eratosthenes_3(i)
    enp = eratosthenes_np(i)
    assert e1 == e2, 'i={}, e1={}, e2={}'.format(i, e1, e2)
    assert e1 == e3, 'i={}, e1={}, e3={}'.format(i, e1, e3)
    assert e1 == enp, 'i={}, e1={}, enp={}'.format(i, e1, enp)

def time_it(func, n=10000000, repeats=10):
    t1 = clock()
    for _ in range(repeats):
        assert len(func(n)) > 100
    t2 = clock()
    print('Time for', str(func), ':', (t2 - t1) / repeats, 'seconds.')

#time_it(eratosthenes_1)
#time_it(eratosthenes_2)
#time_it(eratosthenes_3)
time_it(eratosthenes_np)





















