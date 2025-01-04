# Importing necessary libraries
import streamlit as st
import pandas as pd
from joblib import load
import numpy as np 

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

model_path = r"D:\BIA Project - Stellar Object Classification\BIA_Project_Overall Data\Data\XGBoost.joblib"
try:
    Model = load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}. Please verify the file path.")
    st.stop()  # Stop execution if the model is not found

# Title for the App
st.title("Stellar Object Classification App")

# Add an image to the app
image_path = r"D:\BIA Project - Stellar Object Classification\BIA_Project_Overall Data\Data\Project.png"
try:
    st.image(image_path, caption="Stellar Objects", use_container_width=True)
except Exception as e:
    st.error(f"Error loading image from path: {image_path}. Error: {e}")

# UI for input details
st.header("Enter the details below:")

alpha = st.number_input("Right Ascension angle:", format="%.6f")
delta = st.number_input("Declination angle:", format="%.6f")
u = st.number_input("Enter Ultraviolet filter value:", format="%.6f")
g = st.number_input("Enter green filter value:", format="%.6f")
r = st.number_input("Enter Red filter value:", format="%.6f")
i = st.number_input("Enter Near Infrared filter value:", format="%.6f")
z = st.number_input("Enter Infrared filter value:", format="%.6f")
cam_col = st.selectbox("Camera column", options=(1, 2, 3, 4, 5, 6))
redshift = st.number_input("Enter the redshift value:", format="%.6f")
plate = st.number_input("Enter the Plate ID:", step=1, format="%d")
MJD = st.number_input("Enter the Modified Julian Date:", step=1, format="%d")

# Prediction button
if st.button("Classify Object"):
    # Check if all required inputs are provided
    input_features = [alpha, delta, u, g, r, i, z, cam_col, redshift, plate, MJD]
    if any(val is None or val == 0 for val in input_features):
        st.error("Please fill in all the required fields before making a prediction.")
    else:
        # Prepare input as a 2D array
        input_array = np.array([input_features])

        # Perform prediction
        try:
            prediction = Model.predict(input_array)

            # Display result
            st.header("Prediction Result")
            if prediction[0] == 0:
                st.success("The object is a Galaxy.")
            elif prediction[0] == 1:
                st.success("The object is a Star.")
            else:
                st.success("The object is a QSO.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
