import numpy as np
import matplotlib.pyplot as plt


# Part a)
def convergence_vector(v):
    """
    Returns the partial sums of vector v.
    :param v: list, list of numbers
    :return: list, list of partial sums of v
    """
    # calculate all partial sums up to the maximum number of terms
    term = [(-1) ** k * (1 / (2 * k + 1)) for k in range(max(v))]
    # use list comprehension to iterate over rows of v and assign partial sums to list w
    w = [sum(term[:l + 1]) for l in v]
    return w


v = np.arange(1,11)
w = convergence_vector(v)
print(w)
# Part b)
# generate vector of integers v with list comprehension
v = [2 ** x for x in range(1, 11)]
# calculate partial sums of v
w = convergence_vector(v)
# plot partial sums of v as red dots
plt.plot(v, w, 'ro', label='Partial sums')
# scale the x-axis logarithmically
plt.xscale('log')
# plot the function y = pi/4 as a blue line
plt.plot(v, [np.pi / 4 for i in range(len(v))], '-', label='pi/4')
# add a title, legend, grid and labels to the plot
plt.title('Partial sums of the series')
plt.xlabel('n')
plt.legend()
plt.grid()
# save the plot as a pdf file
plt.savefig('plot_convergence.pdf')


# show the plot by uncommenting the following line
# plt.show()


# Part c)
def convergence_up_to_tolerance(epsilon, m):
    """
    Returns the number of terms needed to reach a tolerance epsilon.
    :param epsilon: int, tolerance
    :param m: int, maximum number of terms
    :return: integer
    """
    # define starting value and previous value
    k = 1
    a_prev = 1
    a = (-1) * (1 / (2 * k + 1))
    # iterate until the difference between the current and previous value is smaller than the tolerance epsilon
    while abs(a - a_prev) > epsilon:
        # create an exit if the maximum number of terms is reached
        if k > m:
            print("The tolerance could not be reached within the given number of terms.")
            return None
        a_prev = a
        a += (-1) ** k * (1 / (2 * k + 1))
        k += 1
    return k


# Example usage
print(convergence_up_to_tolerance(0.0001, 10000))


# Part d)
def partial_sum(N):
    """
    Returns the partial sum of the series up to N terms.
    :param N: int, number of terms
    :return: int, related partial sum
    """
    # make use of the previous defined function convergence_vector
    return convergence_vector([N])[0]


# make use of partial_sum to verify the result of convergence_up_to_tolerance
eps = 0.0001
m = 10000
print((partial_sum(convergence_up_to_tolerance(eps, m))-eps) < np.pi/4 < (partial_sum(convergence_up_to_tolerance(eps, m))+eps))