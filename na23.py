import math


Gamma_D1=2*math.pi*9.765e6 #Hz, not multiplied by 2pi
Gamma_D2=2*math.pi*9.7946e6
Gamma=0.5*(Gamma_D1+Gamma_D2)

lambda_D1=589.755814e-9 #m
lambda_D2=589.158326e-9 #m
omega_D1=3e8/lambda_D1 #Hz
omega_D2=3e8/lambda_D2 #Hz


Isat_D1=186.6 #W/m^2
Isat_D2=62.2 #W/m^2

hf_split=1.77162e9 #Hz