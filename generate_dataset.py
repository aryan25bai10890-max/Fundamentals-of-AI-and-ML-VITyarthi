import pandas as pd
import random

num_samples = 15000

symptoms = [
"fever","cough","headache","vomiting","fatigue","chills",
"nausea","abdominal_pain","dizziness","sweating",
"chest_pain","back_pain","diarrhoea","constipation",
"skin_rash","itching","joint_pain","loss_of_appetite",
"runny_nose","breathlessness"
]

diseases = [
"Flu","Allergy","Migraine","Pneumonia","Malaria",
"Dengue","Typhoid","Diabetes","Hypertension","Common Cold"
]

data = []

for i in range(num_samples):

    row = {symptom: random.randint(0,1) for symptom in symptoms}

    row["prognosis"] = random.choice(diseases)

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("dataset/Training.csv", index=False)

print("Dataset created!")