from data_preprocessing import load_data, preprocess_data, split_data
from feature_engineering import add_internet_ad_budget, adjust_sales_with_internet
from model_training import train_linear_regression, train_random_forest, evaluate_model
from utils import plot_feature_importance, plot_predictions

# Load and preprocess the data
data = load_data('data/advertising_budget_and_sales.csv')
data = preprocess_data(data)

# Feature engineering
data = add_internet_ad_budget(data)
data = adjust_sales_with_internet(data)

# Split the data
X_train, X_test, y_train, y_test = split_data(data, target_column='Adjusted Sales')

# Train models
linear_model = train_linear_regression(X_train, y_train)
random_forest_model = train_random_forest(X_train, y_train)

# Evaluate models
linear_r2 = evaluate_model(linear_model, X_test, y_test)
random_forest_r2 = evaluate_model(random_forest_model, X_test, y_test)

print(f"Linear Regression R²: {linear_r2}")
print(f"Random Forest R²: {random_forest_r2}")

# Plot feature importance for Random Forest
plot_feature_importance(random_forest_model, X_train.columns)

# Plot predictions vs actual values
plot_predictions(y_test, random_forest_model.predict(X_test), title='Random Forest: Actual vs Predicted Sales')