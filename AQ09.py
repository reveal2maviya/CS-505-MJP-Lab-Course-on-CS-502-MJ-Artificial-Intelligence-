"""
Program: Linear Regression
Description: This program implements a simplified linear regression algorithm for educational purposes.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 linear_regression.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python linear_regression.py" to run the program.
"""

# Sample dataset with features and target values
data = [(1, 2), (2, 3), (3, 5), (4, 4), (5, 6)]

# Function to calculate the mean of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Function to calculate the variance of a list of numbers
def variance(values, mean_value):
    return sum([(x - mean_value) ** 2 for x in values])

# Function to calculate the covariance between two lists of numbers
def covariance(x, y, x_mean, y_mean):
    covar = 0
    for i in range(len(x)):
        covar += (x[i] - x_mean) * (y[i] - y_mean)
    return covar

# Function to calculate coefficients (b0, b1) for simple linear regression
def coefficients(data):
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, y, x_mean, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return b0, b1

# Simple linear regression function
def simple_linear_regression(data, test):
    b0, b1 = coefficients(data)
    y_pred = b0 + b1 * test
    return y_pred

# Main function to perform linear regression
def main():
    test_data = 7  # Test data for prediction
    print("Linear Regression:")
    b0, b1 = coefficients(data)
    print(f"Linear Regression Equation: y = {b0:.2f} + {b1:.2f} * x")
    predicted_value = simple_linear_regression(data, test_data)
    print(f"Predicted value for x = {test_data}: y = {predicted_value:.2f}")

if __name__ == '__main__':
    main()
