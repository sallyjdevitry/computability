#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa.py
# description: RSA
# Sally Devitry
# A01980316
##############################################################


import numpy as np
from rsa_aux import xgcd, mod_exp
from rsa_aux import mult_inv, euler_phi, is_prime
import math
import random


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def getRelativePrimeList(n):
    L = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            L.append(i)
    return L

class rsa(object):

    ### Assign 12, subproblem 1.5
    @staticmethod
    def choose_e(eu_phi_n):
        if eu_phi_n >= 20:
            relList = getRelativePrimeList(eu_phi_n)
            sortedRelList = sorted(relList)
            for element in sortedRelList:
                if element <10:
                    sortedRelList.remove(element)
            return random.choice(sortedRelList)

    ### Assign 12, subproblem 1.6
    @staticmethod
    def generate_keys_from_pqe(p, q, e):
        n = p*q
        d = mult_inv(e, (p - 1)*(q - 1))
        pairP = (e, n)
        pairS = (d, n)
        return pairP, pairS

    ### Assign 12, subproblem 1.7    
    @staticmethod
    def encrypt(m, pk):
        (pk1, pk2) = pk
        Pm = m^pk2
        return Pm

    ### Assign 12, subproblem 1.7        
    @staticmethod
    def decrypt(c, sk):
        (sk1, sk2) = sk
        Sc = c^sk2
        return Sc

    ### Assign 12, subproblem 1.8
    @staticmethod
    def encrypt_text(text, pub_key):
        cryptoList = []
        for char in text:
            cryptoList.append(rsa.encrypt(ord(char), pub_key))
        return cryptoList


    ### Assign 12, subproblem 1.8        
    @staticmethod    
    def decrypt_cryptotexts(cryptotexts, sec_key):
        message = ''
        for ctxt in cryptotexts:
            message += chr(rsa.decrypt(ctxt, sec_key))
        return message


