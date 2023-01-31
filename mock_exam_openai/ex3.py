import numpy as np
import matplotlib.pyplot as plt

#Part a)
# Define the number of functions to plot
N = 5

# Create the x values for the plot
x = np.linspace(0, 1, 100)

# Create a 2D array to store the y values of the functions
y = np.zeros((N, x.size))

# Evaluate the functions at each x value and store the results in the y array
for j in range(N):
    y[j] = x**(j+1)

# Plot the functions
plt.figure()
for j in range(N):
    plt.plot(x, y[j], label=f'x^{j+1}')

# Add title, axis labels, grid, and legend
plt.title("Functions x^j for j = 1, ..., N")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

# Save the plot as "xj.png"
plt.savefig("xj.png")

# Save the function values to a file
np.savetxt("my_columns.dat", y.T, delimiter=",", header="x^1,x^2,x^3,x^4,x^5")

# Show the plot
plt.show()

# Part b)
# Load the data from the file
data = np.loadtxt("my_columns.dat", delimiter=",")
x = np.linspace(0, 1, 100)

# Plot the data
plt.figure()
for i in range(data.shape[1]):
    plt.plot(x, data[:,i], label=f'x^{i+1}')

# Add title, axis labels, grid, and legend
plt.title("Functions x^j for j = 1, ..., N")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

# Show the plot
plt.show()
