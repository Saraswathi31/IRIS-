from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the trained model as 'iris_model.pkl'
joblib.dump(model, 'iris_model.pkl')
