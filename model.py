import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# random seed
seed = 1

# Read original dataset
iris = load_iris() 
X = iris.data 
y = iris.target 

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=seed, stratify=y)

# create an instance of the random forest classifier
clf = RandomForestClassifier(n_estimators=100)

# train the classifier on the training data
clf.fit(X_train, y_train)

# predict on the test set
y_pred = clf.predict(X_test)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")  # Accuracy: 0.967

print(f"scikit-learn version used: {sklearn.__version__}")

# save the model to disk
joblib.dump(clf, "rf_model.sav")

with open("rf_model.sav", "rb") as f:
    content = f.read()

# Try to find the version string in the binary
import re
matches = re.findall(b'scikit-learn.*?([0-9]+\.[0-9]+\.[0-9]+)', content)
if matches:
    print("Possible scikit-learn version(s) used:", set(m.decode() for m in matches))
else:
    print("No version string found.")
