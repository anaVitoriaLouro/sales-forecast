import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path, index_col=0)

def preprocess_data(data):
    """Clean and preprocess the data."""
    # Optional: implement any data cleaning steps if needed
    return data

def split_data(data, target_column, test_size=0.3, random_state=42):
    """Splits the dataset into features and target, then into training and testing sets."""
    from sklearn.model_selection import train_test_split
    
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test