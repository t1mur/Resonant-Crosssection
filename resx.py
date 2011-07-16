
import scipy as sp
from scipy import constants
import math
import li6
import na23

hbar=sp.constants.hbar
c=sp.constants.c
pi=math.pi

sigma_D1=3*li6.lambda_D1**2/(2*pi)
sigma_D2=3*li6.lambda_D2**2/(2*pi)

print "*******Lithium 6*********"
print "Ideal sigma D1:", sigma_D1
print "Ideal sigma D2:", sigma_D2, "\n"

IsatC_D1=hbar*li6.omega_D1**3*li6.Gamma/(12*pi*c**2)
IsatC_D2=hbar*li6.omega_D2**3*li6.Gamma/(12*pi*c**2)

print "Isat D1 calc:", IsatC_D1
print "Isat D2 calc:", IsatC_D2, "\n"


print "*******Sodium 23*********"

sigma_D1=3*na23.lambda_D1**2/(2*pi)
sigma_D2=3*na23.lambda_D2**2/(2*pi)

print "Ideal sigma D1:", sigma_D1
print "Ideal sigma D2:", sigma_D2, "Correct! \n"


IsatC_D1=hbar*(na23.omega_D1)**3*na23.Gamma/(12*pi*c**2)
IsatC_D2=hbar*(na23.omega_D2)**3*na23.Gamma/(12*pi*c**2)

print "Isat D1 calc:", IsatC_D1
print "Isat D2 calc:", IsatC_D2, "\n"