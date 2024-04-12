import numpy as np
import matplotlib.pyplot as plt

# Define the range of 'n'
n = np.arange(-1000, 1001)

# Calculate the values of h_lp(n)
h_lp = np.where((n != 0) & (n >= -100) & (n <= 100), 2 * np.sin(n * np.pi / 40) * np.cos(n * 0.342 * np.pi) / (n * np.pi), 0)

# Compute the Discrete Fourier Transform (DFT) of h_lp(n)
h_lp_fft = np.fft.fftshift(np.fft.fft(h_lp))

# Define the frequency axis with respect to omega/pi
N = len(n)
freq = np.fft.fftshift(np.fft.fftfreq(N)) * 2 * np.pi

# Plot the frequency spectrum for w/pi between -0.3 and 0.3
plt.plot(freq / np.pi, np.abs(h_lp_fft), color='blue')
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.xlim(-0.5, 0.5)
plt.grid(True)
plt.savefig('figure6.png')
plt.show()
