#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa_aux.py
# description: auxiliay functions for RSA
# Sally Devitry
# A01980316
##############################################################

import numpy as np
import math

### Assign 12, subproblem 1.1
def xgcd(a,b):
    ''' 
    extended gcd that returns d, x, y such that
    d = ax + by.
    '''
    prevx, x = 1, 0
    prevy, y = 0, 1
    aa, bb = a, b
    while bb != 0:
        q = aa // bb
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        aa, bb = bb, aa % bb
    return aa, prevx, prevy


### Assign 12, subproblem 1.2
def mult_inv(a, n):
    #multiplicative inverse of a in Z^{*}_{n}.
    a = a % n
    for x in range(1, n):
        if ((a * x) % n == 1):
            return x
    return 1

def z_star_sub_n(n):
    #compute the elements of Z^{*}_{n}.
    return np.array([i for i in range(n) if xgcd(i, n) == 1])

### A tool you may want to use in your code (e.g., euler's totient)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 2:
        for d in range(3, int(math.floor(math.sqrt(n)))+1, 2):
            if n % d == 0:
                return False
        return True

def find_primes_in_range(a, b):
    return [i for i in range(a, b+1) if is_prime(i)]

### Assign 12, subproblem 1.3.
def mod_exp(a, b, n):
    #this function computes a^b mod n.
    return (a**b) % n
    # << the above way seems like the simplest way to do it
    #the below (commented) way seems like the way the assignment described it >>
    # c=0
    # d=1
    # binRep = bin(b)[2:]
    # for element in binRep:
    #     c=2*c
    #     d=(d*d) % n
    #     if element == 1:
    #         c=c+1
    #         d=(d*a) % n
    # return d


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

### Assign 12, subproblem 1.4
def euler_phi(n):
    """ Euler's Totient """
    ans = n
    p=2
    while p*p<=n:
        if n%p==0:
            while n%p==0:
                n=n//p
            ans = ans * (1.0-(1.0/float(p)))
        p=p+1
    if n>1:
        ans = ans*(1.0-(1.0/float(n)))
    return int(ans)

