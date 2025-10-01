import pickle
from sklearn.linear_model import LogisticRegression

# Example training data: marks vs pass/fail
X = [[30], [50], [60], [80], [90]]
y = [0, 0, 1, 1, 1]  # 0=Fail, 1=Pass

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
