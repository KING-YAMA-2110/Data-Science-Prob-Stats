import matplotlib.pyplot as plt
import math

def calculate_factorial(n):
    return math.factorial(n)

def stirling_approximation(n):
    x = (n / math.exp(1)) ** n
    y = x * ((2 * (math.pi) * n) ** 0.5)
    return y

def plot_comparison(n_range):
    n_values = list(range(n_range))
    
    # Calculate n! values
    factorial_values = [calculate_factorial(i) for i in n_values]

    # Calculate Stirling's Approximation values
    stirling_values = [stirling_approximation(i) for i in n_values]

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot n vs n!
    axs[0].scatter(n_values, factorial_values, label='n!')
    axs[0].set_title('n vs n!')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('n!')

    # Plot n vs Stirling's Approximation
    axs[1].scatter(n_values, stirling_values, label="Stirling's Approximation", color='orange')
    axs[1].set_title('n vs Stirling\'s Approximation')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel("Stirling's Approximation")

    # Display the plot
    plt.tight_layout()
    plt.show()

# Specify the range for n (up to 50)
n_range = 51
plot_comparison(n_range)
