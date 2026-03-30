import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("dataset/Training.csv")

X = data.drop("prognosis", axis=1)
y = data["prognosis"]

model = RandomForestClassifier()

model.fit(X, y)

pickle.dump(model, open("model/rf_model.pkl", "wb"))

print("Model trained successfully")