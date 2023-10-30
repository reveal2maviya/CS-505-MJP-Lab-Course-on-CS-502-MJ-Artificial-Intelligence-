"""
Program: K-Nearest Neighbor (K-NN) Algorithm
Description: This program implements a simplified K-Nearest Neighbor algorithm for classification.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 k_nearest_neighbor.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python k_nearest_neighbor.py" to run the program.
"""

import math

# Sample dataset with labeled examples (features and labels)
dataset = {
    'example1': {'features': [3, 3], 'label': 'Class A'},
    'example2': {'features': [2, 2], 'label': 'Class A'},
    'example3': {'features': [1, 1], 'label': 'Class B'},
    'example4': {'features': [4, 4], 'label': 'Class B'},
}

# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

# K-NN classification function
def k_nearest_neighbor(data, query, k):
    distances = []
    for example in data:
        distance = euclidean_distance(data[example]['features'], query)
        distances.append((example, distance))

    # Sort the distances and get the K nearest neighbors
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]

    # Count the class labels of the K nearest neighbors
    class_counts = {}
    for neighbor in neighbors:
        label = data[neighbor[0]]['label']
        if label in class_counts:
            class_counts[label] += 1
        else:
            class_counts[label] = 1

    # Determine the most common class label
    most_common_label = max(class_counts, key=class_counts.get)
    return most_common_label

# Main function to perform K-NN classification
def main():
    query_point = [2.5, 2.5]  # The point to classify
    k_value = 3  # The number of nearest neighbors to consider

    print("K-Nearest Neighbor Classification:")
    result = k_nearest_neighbor(dataset, query_point, k_value)
    print(f"Query point {query_point} is classified as '{result}'")

if __name__ == '__main__':
    main()
