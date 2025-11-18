import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation parameters
# -----------------------------

N0 = 10000             # initial number of nuclei
half_life = 5          # half-life in chosen time units
decay_const = np.log(2) / half_life

t_max = 20             # total simulation time
dt = 0.1               # time step
times = np.arange(0, t_max, dt)

# -----------------------------
# Monte Carlo Simulation
# -----------------------------

N_sim = []
N = N0

decay_counts = []   # store number of decays each step (for histogram)

for t in times:
    expected = decay_const * N * dt                 # expected decays
    decays = np.random.poisson(expected)            # random (Poisson)
    decays = min(decays, N)                         # avoid negative
    N -= decays
    N_sim.append(N)
    decay_counts.append(decays)

# -----------------------------
# Theoretical Model
# -----------------------------

N_theory = N0 * np.exp(-decay_const * times)

# -----------------------------
# Plot: Simulation vs Theory
# -----------------------------

plt.figure(figsize=(9, 5))
plt.plot(times, N_sim, label="Monte Carlo N(t)", linewidth=2)
plt.plot(times, N_theory, label="Theoretical N(t)", linestyle="--")
plt.xlabel("Time")
plt.ylabel("Number of nuclei")
plt.title("Radioactive Decay: Monte Carlo vs Theoretical")
plt.legend()
plt.grid(True)

# Save plot
plt.savefig("results/decay_curve.png", dpi=300)
plt.show()

# -----------------------------
# Plot: Histogram of decay counts
# -----------------------------

plt.figure(figsize=(8, 5))
plt.hist(decay_counts, bins=20, edgecolor="black")
plt.xlabel("Number of decays per step")
plt.ylabel("Frequency")
plt.title("Histogram of Poisson Decay Events")
plt.grid(True)

plt.savefig("results/decay_histogram.png", dpi=300)
plt.show()

print("Simulation complete. Plots saved in results/ folder.")
