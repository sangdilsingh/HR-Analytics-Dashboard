import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Data load
df = pd.read_csv(r"C:\Users\dell\OneDrive\Documents\Raw_Data\hr_dataset_100k.csv")

# Attrition ko 0/1 mein convert karo
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Sirf numbers wale columns lenge
features = ['Age', 'ExperienceYears', 'MonthlySalary', 
            'PerformanceRating', 'JobSatisfaction', 
            'WorkLifeBalance', 'TrainingHoursPerYear', 
            'LeavesTaken', 'Promotions']

X = df[features]
y = df['Attrition']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model banao
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy check
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance
import pandas as pd
importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nFeature Importance:")
print(importance)