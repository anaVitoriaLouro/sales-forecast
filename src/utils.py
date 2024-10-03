import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, feature_names):
    """Plot feature importance for the Random Forest model."""
    sns.barplot(x=feature_names, y=model.feature_importances_)
    plt.title('Feature Importance')
    plt.show()

def plot_predictions(y_test, predictions, title='Actual vs Predicted Sales'):
    """Plot the actual sales vs predicted sales."""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.title(title)
    plt.show()