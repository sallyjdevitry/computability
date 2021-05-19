#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: hack_rsa.py
# description: obtaining RSA's secrete key from messages,
# cryptotexts, and public keys.
# Sally Devitry
# A01980316
#############################################################

import math
from rsa_aux import xgcd, mod_exp
from rsa_aux import mult_inv, euler_phi, is_prime
from rsa import rsa

class hack_rsa(object):

    ### Assign 12, subproblem 1.9
    @staticmethod
    def get_sec_key(message, cryptotext, pub_key):
        e, n = pub_key
        d = mult_inv(e, euler_phi(n))
        S = d,n
        return S
