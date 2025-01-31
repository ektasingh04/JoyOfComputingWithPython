import numpy as np
import random 

x=np.array([[1,2,3],[3,4,5]])
a=np.zeros((2,2))
b=np.ones((2,2))
c=np.full((2,2),6)
print(c)
d=np.random.random((2,2))
print("random.random array is ",d)
print(x)
print("sum of x",np.sum(x))
print("sum of x along axis=0",np.sum(x,axis=0)) #col wise sum as axis =0 for row wise sum axis=1
print(np.sum(x,axis=1))
print("Hello EVeryone".lower( ))
'''
#array multiplicn
a=np.array([1,2,3])
b=np.array([[1],[2],[3]])
print(a*b)

#list multiplcn  eroor
a=[1,2,3]
b=[[1],[2],[3]]
print(a*b)



l=[1,4,6,8]
x=np.array(l)
print(x)
print(type(x))'''