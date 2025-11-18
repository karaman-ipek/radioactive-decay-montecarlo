import numpy as np
import matplotlib.pyplot as plt

# Number of radioactive nuclei at t=0
N0 = 10000

# Decay constant (lambda)
# Example: half-life = 5 units
half_life = 5
decay_const = np.log(2) / half_life

# Simulation time parameters
t_max = 20
dt = 0.1
times = np.arange(0, t_max, dt)

# Arrays to store results
N_values = []
N = N0

for t in times:
    # Expected number of decays in time dt
    expected_decays = decay_const * N * dt

    # Number of decays is Poisson-distributed
    decays = np.random.poisson(expected_decays)

    # Update number of nuclei
    N -= decays

    N = max(N, 0)  # cannot go negative
    N_values.append(N)

# Plot result
plt.figure(figsize=(8,5))
plt.plot(times, N_values, label="Simulated N(t)")
plt.xlabel("Time")
plt.ylabel("Number of nuclei")
plt.title("Monte Carlo Radioactive Decay Simulation")
plt.grid()
plt.legend()
plt.show()
