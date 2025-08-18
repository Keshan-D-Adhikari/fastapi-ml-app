import csv
import pickle
import os
try:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import numpy as np
except ImportError:
    print("Please install scikit-learn: pip install scikit-learn numpy")
    exit(1)

def train_model():
    # Load the dataset manually
    X, y = [], []
    with open('data/iris.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            X.append([float(row['sepal_length']), float(row['sepal_width']), 
                     float(row['petal_length']), float(row['petal_width'])])
            y.append(row['species'])
    
    X = np.array(X)
    y = np.array(y)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Save the model
    os.makedirs('models', exist_ok=True)
    with open('models/iris_classifier.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    return model, accuracy

if __name__ == "__main__":
    model, accuracy = train_model()
    print("Model trained and saved successfully!")
