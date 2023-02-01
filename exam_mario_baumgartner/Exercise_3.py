import matplotlib.pyplot as plt
import numpy as np

# Part a)
# load the data from the file as a numpy array
data = np.loadtxt('my_functions.dat', delimiter=',')
# extract and assign the columns of the data to variables x,y,z
x = [row[0] for row in data]
y = [row[1] for row in data]
z = [row[2] for row in data]

# Part b)
# plot the data with one as a straight line and one as a dashed line
plt.plot(x, y, label="y(x)", linestyle="-")
plt.plot(x, z, label="z(x)", linestyle="--")
# add a title, legend, grid and labels to the plot
plt.title("Unknown functions")
plt.xlabel("x")
plt.ylabel("y(x), z(x)")
plt.legend()
plt.grid()
# save the plot as a pdf file
plt.savefig("my_plot.pdf")
# show the plot by uncommenting the following line
# plt.show()

# Part c)
# switch rows y and z in data
data[:, 1] = z
data[:, 2] = y
# create a header for the data
header = "x_n,z_n,y_n"
# save the data to a new file with the new order of rows
np.savetxt("my_switch.dat", data, header=header, delimiter=", ", fmt="%.4f")
