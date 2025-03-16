import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Create x-values
x1 = np.linspace(-2, 2, 100)  # For x^3
x2 = np.linspace(-2*np.pi, 2*np.pi, 100)  # For sin(x)
x3 = np.linspace(0, 2, 100)  # For e^x
x4 = np.linspace(0, 5, 100)  # For log(x+1), x ≥ 0

# Step 3: Compute y-values using given functions
y1 = x1**3  # f(x) = x^3
y2 = np.sin(x2)  # f(x) = sin(x)
y3 = np.exp(x3)  # f(x) = e^x
y4 = np.log(x4 + 1)  # f(x) = log(x+1)

# Step 4: Create a 2×2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

# Step 5: Plot each function in the correct subplot
axs[0, 0].plot(x1, y1, 'r-', linewidth=1.5)  # Top-left (x^3)
axs[0, 0].set_title("f(x) = x³")

axs[0, 1].plot(x2, y2, 'b-', linewidth=1.5)  # Top-right (sin(x))
axs[0, 1].set_title("f(x) = sin(x)")

axs[1, 0].plot(x3, y3, 'g-', linewidth=1.5)  # Bottom-left (e^x)
axs[1, 0].set_title("f(x) = e^x")

axs[1, 1].plot(x4, y4, 'm-', linewidth=1.5)  # Bottom-right (log(x+1))
axs[1, 1].set_title("f(x) = log(x+1)")

# Step 6: Add labels and grid
for ax in axs.flat:
    ax.set_xlabel("x")  # Label for x-axis
    ax.set_ylabel("f(x)")  # Label for y-axis
    ax.grid(True)  # Add grid for better visualization

# Step 7: Display the plots
plt.tight_layout()  # Adjust layout to avoid overlap
plt.show()
