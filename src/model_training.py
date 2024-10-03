from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

def train_linear_regression(X_train, y_train):
    """Train a linear regression model."""
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    return linear_model

def train_random_forest(X_train, y_train):
    """Train a random forest model."""
    random_forest_model = RandomForestRegressor()
    random_forest_model.fit(X_train, y_train)
    return random_forest_model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance."""
    predictions = model.predict(X_test)
    return metrics.r2_score(y_test, predictions)