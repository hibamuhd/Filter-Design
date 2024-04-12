import numpy as np
import matplotlib.pyplot as plt

# Define constants
epsilon = 0.4
N = 4

# Compute theta
theta = np.arcsinh(1 / epsilon) / N

# Compute phi_k for k = 1 to 2N
phi_k = [(2*k - 1) * np.pi / (2 * N) for k in range(1, 2*N+1)]

# Compute poles
poles = []
x_values = []
for k in range(1, 2*N+1):
    pole = -np.sinh(theta) * np.sin(phi_k[k-1]) + 1j * np.cosh(theta) * np.cos(phi_k[k-1])
    poles.append(pole)
    x_values.append(np.real(pole))  # Append the real part of the pole as x value

# Save poles and corresponding x values to a text file
with open('poles.txt', 'w') as file:
    for x, pole in zip(x_values, poles):
        file.write(f'{pole.real} {pole.imag}\n')

# Separate left and right poles
left_poles = [pole for pole in poles if pole.real < 0]
right_poles = [pole for pole in poles if pole.real > 0]

# Plot poles
plt.figure(figsize=(8, 6))
plt.scatter([pole.real for pole in left_poles], [pole.imag for pole in left_poles], c='blue', marker='x', label='Left Poles')
plt.scatter([pole.real for pole in right_poles], [pole.imag for pole in right_poles], c='red', marker='x', label='Right Poles')
plt.title('Poles of the system')
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.xlim(-1.5, 1.5)  # Set x-axis limits from -1.5 to 1.5
plt.ylim(-1.2, 1.2)  # Set y-axis limits from -1.2 to 1.2
plt.grid(True)
plt.legend()
plt.savefig('pole_zero.png')
plt.show()

