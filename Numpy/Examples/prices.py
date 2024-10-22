import numpy as np 
import random as r 

t = np.zeros(5)

print(t)
print(t.dtype)

for i in range(0,len(t) ):
    t[i] = r.randint(10, 26)

print(t)

print( t * 1.1 )

t = t * 1.1

print(t)

print( t > 20 )
print( t[ t > 20 ] )

print ( sum(t > 20) )