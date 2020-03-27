#!/usr/bin/env python3.8

def prime(min, max):
    primes=[]
    for n in range(min, max+1):
        talley=0
        for i in range (1,n+1):
            if n==1 or (n % i == 0 and i != n and i !=1):
                talley=1            
        if talley == 0:
            primes.append(n)
    
    print(primes)

prime(1000,3000)