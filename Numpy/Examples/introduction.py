import numpy as np 
# print( np )
t = np.array([1, 2, 3])

print(t)

print(t.dtype)

r = np.array(["Big data", "Python", "Pandas"])

print(r)
print(r.dtype)

r[0] = "Bonjour tout le monde, comment ça va ?"

print(r)