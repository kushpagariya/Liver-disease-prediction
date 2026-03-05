import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 
import joblib

# Load Data
df = pd.read_csv("Liver_disease_data.csv")

print("First 5 rows:")
print(df.head())
print("\nColumns:")
print(df.columns.tolist())

# Preprocessing
df.fillna(df.mean(numeric_only=True), inplace=True)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Features and Target
X = df.drop('Diagnosis', axis=1)
y = df['Diagnosis']

# Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, 'liver_disease_model.pkl')
joblib.dump(le, 'label_encoder.pkl')

# Save column names
columns = X.columns.tolist()
print("\n✅ Model saved! Copy these columns for frontend:")
print(columns)