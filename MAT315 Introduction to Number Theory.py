# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:41:17 2022

@author: Admin
@topic: MAT315 Introduction to Number Theory
"""
import math

# %% Check if n is prime, return True if is prime, return False if is composite
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True
        
# %% Return all 1 <= k < n such that (k,n)=1
def coprime_list(n):
    lst=[]
    for i in range(1000):
        if math.gcd(n,i)==1:
            lst.append(i)
    return(lst)

# %% Determine if n is a carmichael number, return True if it is, return False if it isn't
def is_carmichael(n):
    lst=coprime_list(n)
    for b in lst:
        if (b**(n-1))%n != 1:
            return False
    return True

# %%# Return the number of units in Zn
def phi(n): 
    m=0
    for i in range(n):
        if math.gcd(i,n)==1:
            m+=1
    #print("phi(n)=",m)
    return m

# %% Return the order of u modulo p
def order(u,n): 
    for k in range(1,n):
        if (u**k)%n==1:
            return k