# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:17:34 2024

@author: Galaxy Book Pro
"""

a=1
b=2
print(a+b)


hungry = True

if hungry:
    print("I'm hungry")
    
hungry = False

if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm slpeey")
    
for i in[1,2,3]:
    print(i)


import numpy as np
x = np.array([1.0,2.0,3.0])
print(x)
type(x)

x=np.array([1.0,2.0,3.0])
y=np.array([2.0,4.0,6.0])
x+y
x-y
x*y
x/y


A=np.array([[1,2],[3,4]])
print(A)
A.shape
A.dtype
B=np.array([[3.0],[0,6]])
A+B


