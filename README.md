# Monte Carlo Radioactive Decay Simulation
## Run Online

Click the button below to launch this project in Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/karaman-ipek/radioactive-decay-montecarlo/HEAD)

This project simulates radioactive decay using a **Monte Carlo approach**, modeling individual decay events based on **Poisson statistics** and the **exponential decay law**.

The simulation tracks the number of undecayed nuclei \( N(t) \) over time and compares the result with the theoretical decay curve.

---

## 🔬 Physics Background

Radioactive decay is a **stochastic (random) process**.  
The probability of a nucleus decaying in a time interval \( dt \) is:

\[
P = \lambda \, dt
\]

where  
- \( \lambda \) = decay constant  
- \( t_{1/2} = \frac{\ln 2}{\lambda} \) = half-life  

The analytical solution is:

\[
N(t) = N_0 e^{-\lambda t}
\]

In this simulation, the number of decays in each time step is generated from a **Poisson distribution**:

\[
\Delta N \sim \text{Poisson}(\lambda N dt)
\]

---

## 🖥 How to Run the Simulation

### Install dependencies:
```bash
pip install numpy matplotlib

python src/main.py
