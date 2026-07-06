import streamlit as st
import pandas as pd
import pickle

# ==========================
# Load Model, Scaler & Encoder
# ==========================
model = pickle.load(open("logistic_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoder = pickle.load(open("labelencoders.pkl", "rb"))

# ==========================
# Streamlit Page Configuration
# ==========================
st.set_page_config(
    page_title="Gender Classification",
    page_icon="👤",
    layout="centered"
)

st.title("👤 Gender Classification using Machine Learning")
st.write("Enter the facial features below and click **Predict**.")

st.markdown("---")

# ==========================
# User Inputs
# ==========================

long_hair = st.selectbox("Long Hair", ["Yes", "No"])
forehead_width = st.number_input(
    "Forehead Width (cm)",
    min_value=10.0,
    max_value=20.0,
    value=13.5
)

forehead_height = st.number_input(
    "Forehead Height (cm)",
    min_value=2.0,
    max_value=10.0,
    value=6.0
)

nose_wide = st.selectbox("Nose Wide", ["Yes", "No"])
nose_long = st.selectbox("Nose Long", ["Yes", "No"])
lips_thin = st.selectbox("Thin Lips", ["Yes", "No"])
distance = st.selectbox("Distance Nose to Lip Long", ["Yes", "No"])

# ==========================
# Convert Yes/No into 1/0
# ==========================

long_hair = 1 if long_hair == "Yes" else 0
nose_wide = 1 if nose_wide == "Yes" else 0
nose_long = 1 if nose_long == "Yes" else 0
lips_thin = 1 if lips_thin == "Yes" else 0
distance = 1 if distance == "Yes" else 0

# ==========================
# Prediction
# ==========================

if st.button("Predict Gender"):

    input_data = pd.DataFrame({
        "long_hair": [long_hair],
        "forehead_width_cm": [forehead_width],
        "forehead_height_cm": [forehead_height],
        "nose_wide": [nose_wide],
        "nose_long": [nose_long],
        "lips_thin": [lips_thin],
        "distance_nose_to_lip_long": [distance]
    })

    # Scale Input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Decode Prediction
    try:
        gender = label_encoder.inverse_transform(prediction)[0]
    except:
        gender = prediction[0]

    st.markdown("---")
    st.success(f"Predicted Gender: **{gender}**")

    if str(gender).lower() == "male":
        st.info("👨 The model predicts **Male**.")
    else:
        st.info("👩 The model predicts **Female**.")

    # Show Input Data
    with st.expander("View Input Data"):
        st.write(input_data)