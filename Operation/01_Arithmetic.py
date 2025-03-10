import numpy as np
x=np.array([2,4,8,10])
y=np.array([4,5,6,7])
addition=np.add(x,y)
subtraction=np.subtract(x,y)
division=np.divide(x,y)
multiplication=np.multiply(x,y)
modulo=np.mod(x,2)
Power=np.power(x,2)
Reciprocal=np.reciprocal(y)
print(addition)
print(subtraction)
print(division)
print(multiplication)
print(modulo)
print(Power)
print(Reciprocal)

""""
[ 6  9 14 17]
[-2 -1  2  3]
[0.5        0.8        1.33333333 1.42857143]
[ 8 20 48 70]
[0 0 0 0]
[  4  16  64 100]
[0 0 0 0]

"""