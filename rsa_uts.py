#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa_uts.py
# author: vladimir kulyukin
# descrip: unit tests for CS5000: F20: HW12
# bugs to vladimir kulyukin via canvas
##############################################################

import unittest
import numpy as np
import random
import math
from rsa_aux import xgcd, mult_inv, z_star_sub_n, euler_phi
from rsa_aux import find_primes_in_range, mult_inv, mod_exp
from rsa import rsa
from hack_rsa import hack_rsa

class rsa_uts(unittest.TestCase):

    ### unit test for subproblem 1.1
    def test_xgcd(self, lwr=1, uppr=1000000, ntests=100000):
        for _ in range(ntests):
            a = random.randint(lwr, uppr)
            b = random.randint(lwr, uppr)
            g, x, y = xgcd(a, b)
            assert g == a*x + b*y
            gcd_bound = int(min(math.sqrt(a), math.sqrt(b)))
            for d in range(g+1, gcd_bound+1):
                assert not (a % d == 0 and b % d == 0)

    ### unit test 1 for subproblem 1.2
    def test_mult_inv_01(self):
        ### 2 * 13 <> 1 (mod 1), so 2 = 13^-1 (mod 5)
        assert 2 == mult_inv(13, 5)
        ### 8 * 5 <> 1 (mod 13), so 8 = 5^-1 (mod 13)
        assert 8 == mult_inv(5, 13)

    ### unit test 2 for subproblem 1.2        
    def test_mult_inv_02(self):
        for a in z_star_sub_n(7):
            assert x == mult_inv(a, 7)
            assert a*x % 7 == 1

    ### unit test 3 for subproblem 1.2                    
    def test_mult_inv_03(self):
        for a in z_star_sub_n(211):
            assert x == mult_inv(a, 211)
            assert a*x % 211 == 1

    ### unit test 1 for subproblem 1.3                                
    def test_mod_exp_01(self):
        for a in z_star_sub_n(211):
            assert x == mult_inv(a, 211)
            assert a*x % 211 == 1
            assert mod_exp(a, 1, 211) == 1

    ### unit test 2 for subproblem 1.3                                
    def test_mod_exp_02(self, numtests=1000):
        for _ in range(numtests):
            a = random.randint(2, 1000)
            b = random.randint(2, 1000)
            n = random.randint(2, 1000)
            assert mod_exp(a, b, n) == (a**b) % n

    ### unit test 1 for subproblem 1.4      
    def test_euler_phi_01(self):
        assert euler_phi(45) == 24        

    ### unit test 2 for subproblem 1.4         
    def test_euler_phi_02(self):
        nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for p in nums:
            assert euler_phi(p) == p-1
        for p in nums:
            for q in nums:
                if p != q:
                    assert euler_phi(p*q) == (p-1)*(q-1)

    ### unit test for subproblem 1.5     
    def test_choose_e(self):
        nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
                47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for p in nums:
            for q in nums:
                if p != q:
                    eu_phi_n = (p-1)*(q-1)
                    if eu_phi_n > 20:
                        e = rsa.choose_e(eu_phi_n)
                        assert xgcd(eu_phi_n, e)[0] == 1

    ### unit test for subproblem 1.6     
    def test_generate_keys_from_pqe(self):
        nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for p in nums:
            for q in nums:
                if p != q:
                    eu_phi_n = (p-1)*(q-1)
                    if eu_phi_n > 20:
                        e = rsa.choose_e(eu_phi_n)
                        public_key, secret_key = rsa.generate_keys_from_pqe(p, q, e)
                        assert len(public_key) == len(secret_key) == 2
                        n = p*q
                        assert e == public_key[0] and public_key[1] == n
                        d = mult_inv(e, eu_phi_n)
                        assert d == secret_key[0] and secret_key[1] == n
                        
    ### unit test 1 for subproblem 1.7
    def test_encrypt_decrypt_01(self):
        p, q, e = 11, 29, 3
        epn = euler_phi(p*q)
        assert epn == (11-1)*(29-1)
        assert xgcd(epn, 3)[0] == 1
        pk, sk = rsa.generate_keys_from_pqe(p, q, e)
        M = 100
        assert rsa.decrypt(rsa.encrypt(M, pk), sk) == M
        assert rsa.encrypt(rsa.decrypt(M, sk), pk) == M

    ### unit test 2 for subproblem 1.7 
    def test_encrypt_decrypt_02(self):
        nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for p in nums:
            for q in nums:
                if p != q:
                    eu_phi_n = (p-1)*(q-1)
                    if eu_phi_n > 20:
                        e = rsa.choose_e(eu_phi_n)
                        n = p*q
                        M = random.randint(0, n-1)
                        pk, sk = rsa.generate_keys_from_pqe(p, q, e)
                        assert rsa.decrypt(rsa.encrypt(M, pk), sk) == M
                        assert rsa.encrypt(rsa.decrypt(M, sk), pk) == M

    ### unit test 1 for subproblem 1.8 
    def test_encrypt_decrypt_text_01(self):
        text = 'Everything is a number.\n\n' + \
                  '                Pythagoras\n'
        pub_key = (116209, 415733)
        sec_key = (231097, 415733)
        cryptotexts = rsa.encrypt_text(text, pub_key)
        print('Cryptotexts:\n')
        print(cryptotexts)
        decrypted_text = rsa.decrypt_cryptotexts(cryptotexts, sec_key)
        print('\nOriginal Text:\n')
        print(text)
        print('Decrypted Text:\n')        
        print(decrypted_text)
        assert text == decrypted_text

    ### unit test 2 for subproblem 1.8         
    def test_encrypt_decrypt_text_02(self):
        text = 'I am by heritage a Jew, by citizenship a Swiss,\n' + \
               'and by makeup a human being, and only a human being,\n' + \
               'without any special attachment to any state or national\n' + \
               'entity whatsoever.\n' + \
               '\n\n' + \
               '                Albert Einstein\n'
        pub_key = (116209, 415733)
        sec_key = (231097, 415733)
        cryptotexts = rsa.encrypt_text(text, pub_key)
        print('Cryptotexts:\n')
        print(cryptotexts)
        decrypted_text = rsa.decrypt_cryptotexts(cryptotexts, sec_key)
        print('\nOriginal Text:\n')
        print(text)
        print('Decrypted Text:\n')        
        print(decrypted_text)
        assert text == decrypted_text

    ### unit test 1 for subproblem 1.9         
    def test_hack_rsa_01(self):
        print('\n***** Hacking 2-digit pq...')
        ## p and q are 2-digit primes
        p, q, e = 11, 29, 3
        pk, sk = rsa.generate_keys_from_pqe(p, q, e)
        M = 100
        C = rsa.encrypt(M, pk)
        hacked_sk = hack_rsa.get_sec_key(M, C, pk)
        assert sk[0] == hacked_sk[0] and sk[1] == hacked_sk[1]
        print('original key = {}'.format(sk))
        print('hacked key   = {}'.format(hacked_sk))
        print('***** Hacking 2-digit pq done...')

    ### unit test 2 for subproblem 1.9
    def test_hack_rsa_02(self):
        print('\n***** Hacking 3-digit pq...')
        ## p and q are 3-digit primes
        p, q = 397, 883
        epn = euler_phi(p*q)
        e = rsa.choose_e(epn)
        pk, sk = rsa.generate_keys_from_pqe(p, q, e)
        print('pk = {}'.format(pk))
        print('sk = {}'.format(sk))
        M = 100
        C = rsa.encrypt(M, pk)
        hacked_sk = hack_rsa.get_sec_key(M, C, pk)
        assert sk[0] == hacked_sk[0] and sk[1] == hacked_sk[1]
        print('original sk = {}'.format(sk))
        print('hacked   sk = {}'.format(hacked_sk))
        print('***** Hacking 3-digit pq done...')

    ### unit test 3 for subproblem 1.9
    # def test_hack_rsa_03(self):
    #     print('\n***** Hacking 4-digit pq...')
    #     ## p and q are 4-digit primes
    #     p, q = 8629, 9973
    #     epn = euler_phi(p*q)
    #     e = rsa.choose_e(epn)
    #     pk, sk = rsa.generate_keys_from_pqe(p, q, e)
    #     print('pk = {}'.format(pk))
    #     print('sk = {}'.format(sk))
    #     M = 100
    #     C = rsa.encrypt(M, pk)
    #     hacked_sk = hack_rsa.get_sec_key(M, C, pk)
    #     assert sk[0] == hacked_sk[0] and sk[1] == hacked_sk[1]
    #     print('original sk = {}'.format(sk))
    #     print('hacked   sk = {}'.format(hacked_sk))
    #     print('***** Hacking 4-digit pq done...')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
