
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# -------------------------------------------------
# Load models (cached)
# -------------------------------------------------
@st.cache_resource
def load_laptop_model():
    return joblib.load("price_model.pkl")

@st.cache_resource
def load_car_model():
    return tf.keras.models.load_model("car_price_model.keras")


# -------------------------------------------------
# App title
# -------------------------------------------------
st.set_page_config(page_title="Price Prediction App", layout="centered")
st.title("💰 Multi Price Prediction App")

# -------------------------------------------------
# Select prediction type
# -------------------------------------------------
prediction_type = st.radio(
    "Select Prediction Type:",
    ["Laptop Price", "Car Price"]
)

# =================================================
# LAPTOP PREDICTION SECTION
# =================================================
if prediction_type == "Laptop Price":

    model = load_laptop_model()
    preprocessor = model.named_steps["preprocess"]
    raw_columns = preprocessor.feature_names_in_

    st.subheader("💻 Laptop Details")

    # -------- CONFIG --------
    binary_cols = [
        "has_ssd",
        "has_hdd",
        "has_flash",
        "has_hybrid",
        "is_ips",
        "is_touch",
        "is_retina",
        "is_4k"
    ]

    screen_pixel_map = {
        "2560×1600": 4096000,
        "1440×900": 1296000,
        "1920×1080": 2073600,
        "2880×1800": 5184000,
        "1366×768": 1049088,
        "2560×1296": 3317760,
        "3200×1800": 5760000,
        "1920×1200": 2304000,
        "1848×1836": 3393024,
        "3840×2160 (4K)": 8294400,
        "2560×1215": 3110400,
        "2560×1440": 3686400,
        "1200×1200": 1440000,
        "2736×1824": 4990464,
        "2400×1600": 3840000
    }

    input_data = {}

    for col in raw_columns:

        if col in binary_cols:
            choice = st.selectbox(col, ["No", "Yes"])
            input_data[col] = 1 if choice == "Yes" else 0

        elif col == "screen_pixels":
            resolution = st.selectbox(
                "Screen Resolution",
                list(screen_pixel_map.keys())
            )
            input_data[col] = screen_pixel_map[resolution]

        else:
            input_data[col] = st.text_input(col)

    if st.button("Predict Laptop Price"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        st.success(f"Predicted Laptop Price: € {prediction:,.2f}")


# =================================================
# CAR PREDICTION SECTION
# =================================================
elif prediction_type == "Car Price":

    model = load_car_model()

    st.subheader("🚗 Car Details")

    years = st.number_input("Years Used", min_value=0)
    km = st.number_input("Kilometers Driven", min_value=0)
    rating = st.number_input("Rating", min_value=0)
    condition = st.number_input("Condition Score", min_value=0)
    economy = st.number_input("Mileage (km/l)", min_value=0.0)
    top_speed = st.number_input("Top Speed", min_value=0)
    hp = st.number_input("Horsepower", min_value=0)
    torque = st.number_input("Torque", min_value=0)

    if st.button("Predict Car Price"):

        input_data = np.array([[
            years,
            km,
            rating,
            condition,
            economy,
            top_speed,
            hp,
            torque
        ]], dtype=np.float32)

        prediction = model.predict(input_data)

        st.success(f"Predicted Car Price: ₹ {prediction[0][0]:,.2f}")
