# coding: utf-8

import os, sys
import numpy as np
from math import exp, sqrt, pi

def factorial(n):
    value = 1
    for i in range(n,1,-1):
        value *= i
    return value
  
def double_factorial(n):
    k = 1
    for i in range(n, 1, -2):
        k *= i
    #print("n:", n, "double factorial:", k)
    return k

"""\int_0^\infty r^m e^{-alpha * r^2} dr"""
def gaussian_integral(alpha, m):
    if int(m/2)*2 == m: # even number
        n = int(m/2)
        value = double_factorial(2*n-1) * sqrt(pi) / pow(2, n+1) / pow(alpha, n+0.5)
    else:
        n = int((m-1)/2)
        value = factorial(n) / 2 / pow(alpha, n+1)
    return value

def overlap_s_gaussians(expo1, expo2, power_of_r):
    norm1 = pow(2*expo1/pi, 0.75)
    norm2 = pow(2*expo2/pi, 0.75)
    value = norm1 * norm2 * 4 * pi * gaussian_integral(expo1+expo2, power_of_r+2)
    return value

