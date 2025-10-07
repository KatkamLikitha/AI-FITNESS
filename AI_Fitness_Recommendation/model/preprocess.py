import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv('../data/fitness_data.csv')
X = data[['Age', 'Weight', 'Height', 'Goal']]
y = data[['Workout', 'Diet', 'Tips']]
model = RandomForestClassifier()
model.fit(X, y.values.ravel())
pickle.dump(model, open('fitness_model.pkl', 'wb'))