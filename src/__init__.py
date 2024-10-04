from data_preprocessing import load_data, preprocess_data, split_data
from feature_engineering import add_internet_ad_budget, adjust_sales_with_internet
from model_training import train_linear_regression, train_random_forest, evaluate_model
from utils import plot_feature_importance, plot_predictions

# Load and preprocess the original data
data = load_data('data/advertising_budget_and_sales.csv')
data = preprocess_data(data)

# 1. Process and evaluate models with the original data
print("=== Evaluating Models with Original Data ===")
X_train, X_test, y_train, y_test = split_data(data, target_column='Sales ($)')

# Train models on the original data
linear_model_original = train_linear_regression(X_train, y_train)
random_forest_model_original = train_random_forest(X_train, y_train)

# Evaluate models on the original data
linear_r2_original = evaluate_model(linear_model_original, X_test, y_test)
random_forest_r2_original = evaluate_model(random_forest_model_original, X_test, y_test)

# Print results for the original dataset
print(f"Linear Regression R² (Original Data): {linear_r2_original}")
print(f"Random Forest R² (Original Data): {random_forest_r2_original}")

# 2. Add the 'Internet Ad Budget' feature and adjust the sales, then evaluate models
print("\n=== Evaluating Models with Adjusted Data (including Internet Ad Budget) ===")
data_with_internet = add_internet_ad_budget(data)
data_with_internet = adjust_sales_with_internet(data_with_internet)

X_train_adjusted, X_test_adjusted, y_train_adjusted, y_test_adjusted = split_data(data_with_internet, target_column='Adjusted Sales')

# Train models on the adjusted data
linear_model_adjusted = train_linear_regression(X_train_adjusted, y_train_adjusted)
random_forest_model_adjusted = train_random_forest(X_train_adjusted, y_train_adjusted)

# Evaluate models on the adjusted data
linear_r2_adjusted = evaluate_model(linear_model_adjusted, X_test_adjusted, y_test_adjusted)
random_forest_r2_adjusted = evaluate_model(random_forest_model_adjusted, X_test_adjusted, y_test_adjusted)

# Print results for the adjusted dataset
print(f"Linear Regression R² (Adjusted Data): {linear_r2_adjusted}")
print(f"Random Forest R² (Adjusted Data): {random_forest_r2_adjusted}")

# Plot feature importance and predictions for the adjusted Random Forest model
#plot_feature_importance(random_forest_model_adjusted, X_train_adjusted.columns)
#plot_predictions(y_test_adjusted, random_forest_model_adjusted.predict(X_test_adjusted), title='Random Forest: Actual vs Predicted Sales (Adjusted Data)')