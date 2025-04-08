import numpy as np
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Loads data from a file.
    
    Args:
        file_path (str): The path to the file containing the data.

    Returns:
        X (numpy.ndarray): Feature matrix.
        y (numpy.ndarray): Target vector.
    """
    # Assuming the data is in CSV format
    data = np.genfromtxt(file_path, delimiter=',')
    return data

def split_data(X, y):
    """
    Splits the data into training and testing sets.

    Args:
        X (numpy.ndarray): Feature matrix.
        y (numpy.ndarray): Target vector.

    Returns:
        X_train, y_train: Training feature matrix and target vector.
        X_test, y_test: Testing feature matrix and target vector.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, y_train, X_test, y_test

# Example usage
if __name__ == "__main__":
    file_path = "path_to_your_data.csv"
    
    # Load data
    x_data = load_data(file_path)
    print("Feature matrix:", x_data.shape)
    
    # Split the dataset into training and testing sets
    X_train, y_train, X_test, y_test = split_data(x_data, np.ones(len(y_train)))
    print("Training feature matrix:", X_train.shape)
    print("Testing feature matrix:", X_test.shape)
    print("Target vector:", y_train)
