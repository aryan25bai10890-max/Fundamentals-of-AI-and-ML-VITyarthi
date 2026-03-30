import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="AI Disease Predictor",
    page_icon="🩺",
    layout="wide"
)

# Load model
model = pickle.load(open("model/rf_model.pkl","rb"))

# Load dataset
data = pd.read_csv("dataset/Training.csv")

symptoms = list(data.columns[:-1])

# ------------------------------
# Header
# ------------------------------

st.title("🩺 AI Disease Prediction System")

st.markdown(
"""
This system predicts possible diseases based on symptoms using a machine learning model.
"""
)

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.header("Select Symptoms")

selected_symptoms = st.sidebar.multiselect(
    "Choose symptoms you are experiencing",
    symptoms
)

predict_button = st.sidebar.button("Predict Disease")

# ------------------------------
# Main Layout
# ------------------------------

col1, col2 = st.columns(2)

# Prediction
if predict_button:

    input_data = [
        1 if symptom in selected_symptoms else 0
        for symptom in symptoms
    ]

    prediction = model.predict([input_data])[0]

    probabilities = model.predict_proba([input_data])[0]

    with col1:

        st.subheader("Prediction Result")

        st.success(f"Most likely disease: **{prediction}**")

        st.info(
        "⚠️ This AI prediction is for educational purposes only."
        )

    with col2:

        st.subheader("Prediction Confidence")

        prob_df = pd.DataFrame({
            "Disease": model.classes_,
            "Probability": probabilities
        })

        prob_df = prob_df.sort_values(
            by="Probability",
            ascending=False
        )

        st.bar_chart(prob_df.set_index("Disease"))

else:

    st.write("Select symptoms from the sidebar and click **Predict Disease**.")

# ------------------------------
# Footer
# ------------------------------

st.markdown("---")

st.markdown(
"""
### About this project

This project demonstrates how machine learning can assist in disease prediction based on symptoms.
"""
)