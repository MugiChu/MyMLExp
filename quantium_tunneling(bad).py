import math

k_plank = 6.626e-34

k_electron_mass = 9.1e-31
k_ev = 1.6e-19
e = 4.5
v = 5.0
delta = v - e
size = 1.30e-9
p1 = ((-4 * size * math.pi) / k_plank)
p2 = math.sqrt(2*k_electron_mass*delta*k_ev)
print (p1*p2)