import streamlit as st
import pandas as pd
import numpy as np
from concrete.ml.sklearn import LinearRegression
from sklearn.preprocessing import StandardScaler
import time

# Load model artifacts
@st.cache_data
def load_model():
    # Simulate trained model
    model = LinearRegression(n_bits=8)
    # For simplicity, simulate training
    X = np.random.rand(100, 100).astype(np.float32)
    y = np.random.rand(100).astype(np.float32)
    model.fit(X, y)
    model.compile(X)
    return model, StandardScaler().fit(X)

model, scaler = load_model()

st.title("FHE-based Biological Age Predictor")

uploaded_file = st.file_uploader("Upload DNA methylation CSV file (samples x CpG sites)", type="csv")

if uploaded_file:
    input_df = pd.read_csv(uploaded_file)
    st.write("Uploaded data shape:", input_df.shape)

    try:
        X_input = input_df.values.astype(np.float32)
        X_scaled = scaler.transform(X_input)

        # Predict
        st.subheader("🔒 Encrypted Biological Age Prediction")
        with st.spinner("Running FHE prediction..."):
            start = time.time()
            y_pred = model.predict(X_scaled, fhe="execute")
            duration = time.time() - start

        st.success(f"FHE prediction completed in {duration:.2f} seconds.")
        st.write("📊 Predicted Biological Ages:")
        st.write(y_pred)
    except Exception as e:
        st.error(f"Error during prediction: {e}")