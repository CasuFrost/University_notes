# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:05:17 2023

@author: mcasu
"""
import math

def ric(m,n):
    if m==n==1:
        return 0
    if m>1 and n>1:
        return 4+ric(m-1,n)+ric(m,n-1)
    if m>1:
        return 2+ric(m-1,n)
    return 2+ric(m,n-1)


print("m * n  =  mn -> result")
x=0
y = 0
for i in range(2,20):
		if i%2==0:
			x+=1
		else:
			y+=1
		if x+y>3:
			print(x,"*",y," = ",x*y,"->",ric(x,y))
           