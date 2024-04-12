import numpy as np
import matplotlib.pyplot as plt

# Define the range of 'n'
n = np.arange(-1000, 1001)

# Calculate the values of h_lp(n)
h_lp = np.where((n != 0) & (n >= -100) & (n <= 100), np.sin(n * np.pi / 40) / (n * np.pi), 0)

# Compute the Discrete Fourier Transform (DFT) of h_lp(n)
h_lp_fft = np.fft.fftshift(np.fft.fft(h_lp))

# Define the frequency axis with respect to omega/pi
N = len(n)
freq = np.fft.fftshift(np.fft.fftfreq(N)) * np.pi

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot the frequency spectrum for w/pi between -0.3 and 0.3
axs[0].plot(freq / np.pi, np.abs(h_lp_fft), color='blue')
axs[0].set_xlabel('$\omega/\pi$')
axs[0].set_ylabel('$|H_{lp}(\omega)|$')
axs[0].set_xlim(-0.3, 0.3)  # Limit the x-axis from -0.3 to 0.3 for w/pi
axs[0].grid(True)

# Plot the function itself
axs[1].stem(n, h_lp, linefmt='r-', markerfmt='ro', basefmt='r')
axs[1].set_xlabel('$n$')
axs[1].set_xlim(-120, 120)
axs[1].set_ylabel('$h_{lp}(n)$')
axs[1].grid(True)
plt.tight_layout()
plt.savefig('figure5.png')
plt.show()


