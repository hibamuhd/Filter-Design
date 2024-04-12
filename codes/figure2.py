import numpy as np
import matplotlib.pyplot as plt

# Define the range of Omega values
Omega = np.linspace(0, 2, 100)
Omega_L = np.linspace(0, 2, 100)

# Define the function p(Omega)
def p(Omega):
    return np.where(Omega < 1, np.cos(4 * np.arccos(Omega)), np.cosh(4 * np.arccosh(Omega)))

# Define the function q(Omega)
def q(Omega):
    return 1 / np.sqrt(1 + 0.16 * p(Omega)**2)
        
# Define the function H_a,LP(jOmega_L)
c4 = 8 * Omega_L**4 - 8 * Omega_L**2 + 1
H_squared = 1 / (1 + 0.16 * c4**2)
H = np.sqrt(H_squared)

# Define the function H_a,LP(s_L)
s_L = 1j * Omega_L
numerator = 0.3125
denominator = [1, 1.1068, 1.6125, 0.9140, 0.3366]
H_s_L = numerator / np.polyval(denominator, s_L)

# Plot the function q(Omega) using a scatter plot
plt.figure()
plt.scatter(Omega, q(Omega), color='blue', marker='o', facecolors='none', edgecolors='blue')

# Plot the second function (modulus plot)
plt.plot(Omega_L, np.abs(H_s_L), color='blue')

plt.xlabel('$\Omega_L$')
plt.ylabel('$|H_{a,LP}(j\Omega_L)|$')
plt.legend(['Design', 'Specification'], loc='best')
plt.grid(False)
plt.savefig('figure2.png')
plt.show()


