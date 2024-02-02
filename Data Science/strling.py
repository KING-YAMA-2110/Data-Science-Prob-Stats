import matplotlib.pyplot as plt
import math

def calculate_factorial(n):
    return math.factorial(n)

def stirling_approximation(n):
    x = (n / math.exp(1)) ** n
    y = x * ((2 * (math.pi) * n) ** 0.5)
    return y

def plot_comparison(n_range):
    # Section 1: Creating lists for n and n!
    n_values = list(range(n_range))
    factorial_values = [calculate_factorial(i) for i in n_values]

    # Section 2: Plotting n vs n!
    plt.scatter(n_values, factorial_values, label='n!')

    # Section 3: Creating a list for Stirling's Approximation
    stirling_values = [stirling_approximation(i) for i in n_values]

    # Section 4: Plotting n vs Stirling's Approximation
    plt.scatter(n_values, stirling_values, label="Stirling's Approximation")

    # Adding labels and legend
    plt.xlabel('n')
    plt.ylabel('Value')
    plt.legend()
    
    # Displaying the plot
    plt.show()

# Specify the range for n
n_range = 8
plot_comparison(n_range)
