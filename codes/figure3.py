import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, I, Abs

# Define symbolic variables
s, s_L, Omega_0, B = symbols('s s_L Omega_0 B')

# Given transfer function
H_s_L = 0.3125 / (s_L**4 + 1.1068*s_L**3 + 1.6125*s_L**2 + 0.9140*s_L + 0.3366)

# Define values for Omega_0 and B
Omega_0_val = 0.5945
B_val = 0.1066

# Substitution for s_L
s_L_expr = (s**2 + Omega_0_val**2) / (B_val * s)
H_s = H_s_L.subs(s_L, s_L_expr)

# Modulus of the resultant function at s = j0.5095
s_value = 0.6502*I
modulus_H = Abs(H_s.subs(s, s_value))

# For plotting purposes
# Define the symbolic expression for H_s with specific values of Omega_0 and B
H_s_specific = H_s.subs({Omega_0: Omega_0_val, B: B_val})

# Plot the modulus for a range of frequencies
Omega_values = np.linspace(-0.8, 0.8, 1000)
modulus_values = np.abs(np.array([H_s_specific.subs(s, 1j*Omega) for Omega in Omega_values]))
plt.plot(Omega_values, modulus_values)
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.ylim([0, 1.4])
plt.grid(True)
plt.savefig('figure3.png')
plt.show()
