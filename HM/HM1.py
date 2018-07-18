# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 12:26:35 2018

@author: yinjiang

your program should restrict itself to multiplying only pairs of single-digit numbers. 
implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some 
small test cases of your own devising. Then post your best test cases to the 
discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. 
Does this make your life easier? Does it depend on which algorithm you're 
implementing?]

"""

def KaratMultiplier(in1, in2):
    n1=len(str(in1))
    n2=len(str(in2))
    # base case
    if n1 == 1 or n2 == 1:
        return in1*in2
    else:
        n_2 = max(n1,n2)//2
        
        a = in1//10**(n_2)
        b = in1%10**(n_2)
        c = in2//10**(n_2)
        d = in2%10**(n_2)
        
        ac = KaratMultiplier(a,c)
        bd = KaratMultiplier(b,d)
        ad_bc = KaratMultiplier((a+b),(c+d)) -ac -bd
        result = 10**(2*n_2)*ac+bd+10**(n_2)*ad_bc
        
        return result
        
        
    
    
    