# @Author: Ibrahim Bashir
# @github: https://github.com/polarvapourer
# @Linkedin: www.linkedin.com/in/mohammed-ibrahim-bashir-a01962315
# @Date: 19 November 2026
# @Version: 1
# The program shows how shuffling a time series can disrupt its relationship with another signal while leaving its histogram unchanged.

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
time = np.arange(120)     # Time steps 0 to 119
period = 40               # One full wave takes 40 steps
delay = 4                 # Signal B follows A four steps later

signal_a = np.sin(2 * np.pi * time / period)

noise = rng.normal(0, 0.12, size=len(time))
signal_b = np.sin(2 * np.pi * (time - delay) / period) + noise

plt.figure(figsize=(10, 3))
plt.plot(time, signal_a, label="A: original wave")
plt.plot(time, signal_b, label="B: delayed, noisy copy")
plt.xlabel("Time step")
plt.ylabel("Signal value")
plt.title("Artificial signals before shuffling")
plt.legend()
plt.show()

shuffled_b = rng.permutation(signal_b)

plt.figure(figsize=(10, 3))
plt.plot(time, signal_a, label="A: original wave")
plt.plot(time, shuffled_b, label="B: shuffled copy")
plt.xlabel("Time step")
plt.ylabel("Signal value")
plt.title("Artificial signals after shuffling B")
plt.legend()
plt.show()

bins = np.linspace(signal_b.min(), signal_b.max(), 16)  # 15 ranges

fig, axes = plt.subplots(1, 2, figsize=(9, 3), sharex=True, sharey=True)

axes[0].hist(signal_b, bins=bins, edgecolor="white")
axes[0].set_title("B before shuffling")

axes[1].hist(shuffled_b, bins=bins, edgecolor="white")
axes[1].set_title("B after shuffling")

axes[0].set_ylabel("Number of values")
fig.supxlabel("Signal value")
fig.suptitle("Artificial data")
plt.tight_layout()
plt.show()

a_earlier = signal_a[:-delay]         # A from step 0 to 115
b_later = signal_b[delay:]            # B from step 4 to 119
shuffled_later = shuffled_b[delay:]   # Same steps after shuffling

before = np.corrcoef(a_earlier, b_later)[0, 1]
after = np.corrcoef(a_earlier, shuffled_later)[0, 1]

print(f"Before shuffling: {before:.2f}")
print(f"After shuffling:  {after:.2f}")

