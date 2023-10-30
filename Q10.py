"""
Program: Decision Tree Classifier
Description: This program implements a simplified decision tree classifier for educational purposes.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 decision_tree.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python decision_tree.py" to run the program.
"""

# Sample dataset with features and labels
data = [
    (2, 0),
    (3, 0),
    (5, 1),
    (7, 1),
    (10, 0)
]

# Function to split a dataset into two parts based on a feature and value
def split_dataset(data, feature, value):
    left, right = list(), list()
    for row in data:
        if row[feature] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Function to calculate the Gini index for a split dataset
def gini_index(groups, classes):
    total_samples = float(sum(len(group) for group in groups))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / total_samples)
    return gini

# Function to find the best split point for a dataset
def get_split(data):
    class_values = list(set(row[-1] for row in data))
    b_feature, b_value, b_score, b_groups = 999, 999, 999, None
    for feature in range(len(data[0]) - 1):
        for row in data:
            groups = split_dataset(data, feature, row[feature])
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_feature, b_value, b_score, b_groups = feature, row[feature], gini, groups
    return {'feature': b_feature, 'value': b_value, 'groups': b_groups}

# Function to create a terminal node with the most common class value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Function to create child splits for a node or make a terminal node
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Function to build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Function to make a prediction with a decision tree
def predict(node, row):
    if row[node['feature']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Function to perform classification with a decision tree
def decision_tree_classifier(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = [predict(tree, row) for row in test]
    return predictions

# Main function to perform decision tree classification
def main():
    test_data = [(4, 1), (8, 0)]  # Test data for classification
    max_depth = 3  # Maximum depth of the decision tree
    min_size = 2  # Minimum number of samples in a node

    print("Decision Tree Classifier:")
    predictions = decision_tree_classifier(data, test_data, max_depth, min_size)
    for i in range(len(test_data)):
        print(f"Data {test_data[i]} is classified as {predictions[i]}")

if __name__ == '__main__':
    main()
