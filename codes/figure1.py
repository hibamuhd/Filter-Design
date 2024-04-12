import numpy as np
import matplotlib.pyplot as plt

# Define the range and step size for epsilon
epsilon_range = np.round(np.arange(0.35, 0.61, 0.05), 2)

# Define the range of Omega_L values
Omega_L = np.linspace(0, 2, 1000)

# Calculate the function values for different epsilon values
function_values = {}
for epsilon in epsilon_range:
    # Calculate the function values for the current epsilon value
    cN_squared = (8*Omega_L**4 - 8*Omega_L**2 + 1)**2  # c_4(x) = 8x^4 - 8x^2 + 1
    H = 1 / np.sqrt(1 + epsilon**2 * cN_squared)
    
    # Store the function values
    function_values[epsilon] = H

# Plot the function for different epsilon values
plt.figure()
for epsilon in epsilon_range:
    plt.plot(Omega_L, function_values[epsilon], label=f'$\epsilon$ = {epsilon}', linewidth=1)

plt.xlabel('$\Omega_L$')
plt.ylabel('$|H_{a,LP}(j\Omega_L)|$')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('figure1.png')
plt.show()
