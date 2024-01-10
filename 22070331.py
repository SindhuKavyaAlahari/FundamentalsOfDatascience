# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    """
    Read data from a CSV file.

    Parameters:
    - filename (str): The name of the CSV file containing salary data.

    Returns:
    - pandas.DataFrame: A DataFrame containing the salary
    data with column name 'Salary'.
    """
    return pd.read_csv(filename , header = None , names = ['Salary'])

def plot_histogram(data , bins = 20):
    """Plot histogram."""
    plt.hist(data['Salary'] , bins = bins , density = True , alpha = 0.7 ,
             color = 'lightgreen' , edgecolor = 'black')

def plot_pdf_curve(data):
    """
        Plot histogram of salary distribution.

        Parameters:
        - data (pandas.DataFrame): DataFrame containing the salary
        data with a 'Salary' column.
        - bins (int, optional): Number of bins for the histogram.
        Default is 20.

        Returns:
        - None"""
    mu , std = np.mean(data['Salary']) , np.std(data['Salary'])
    x = np.linspace(min(data['Salary']) , max(data['Salary']) , 100)
    p = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * std**2))
    plt.plot(x , p , 'k' , linewidth = 2 , label = 'PDF Curve')

def add_vertical_lines(mean, X):
    """
    Add vertical lines to a plot representing the mean salary and X value.

    Parameters:
    - mean (float): The mean salary value.
    - X (float): The specified value used in the analysis.

    Returns:
    - None"""
    plt.axvline(mean , color = 'red' , linestyle = 'dashed' , linewidth = 2 ,
                label = 'Mean Salary')
    plt.axvline(X , color = 'green' , linestyle = 'dashed' , linewidth = 2 ,
                label = 'X')

def customize_plot_labels():
    """
    Customize plot labels, title, and legend for salary distribution analysis.

    Returns:
    - None"""
    plt.xlabel('Annual Salary (Euros)' , fontweight = 'bold')
    plt.ylabel('Probability Density' , fontweight = 'bold')
    plt.title('Salary Distribution Analysis' , fontweight = 'bold')
    plt.legend()

def show_plot():
    """
    Display the current plot.

    Returns:
    - None: The function shows the current plot.
    """
    plt.show()

def print_calculated_values(mean_salary , X):
    """
    Print calculated mean salary and X values.

    Parameters:
    - mean_salary (float): The mean salary value.
    - X (float): The calculated value based on specific criteria.

    Returns:
    - None: The function prints the calculated values.
    """
    print(f"Mean Salary (W): {mean_salary:.2f} Euros")
    print(f"Value X: {X:.2f} Euros")

#Read data from file
filename = 'data1-1.csv'
data = read_data(filename)

# Calculate mean salary (W) and X
mean_salary = np.mean(data['Salary'])
X = np.percentile(data['Salary'] , 33)

# Plot histogram and PDF curve
plot_histogram(data)
plot_pdf_curve(data)

# Add vertical lines for mean and X
add_vertical_lines(mean_salary , X)

# Customize plot labels and titles
customize_plot_labels()

# Save and show the plot
show_plot()

# Print calculated values
print_calculated_values(mean_salary , X)
