import os
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from concrete.ml.sklearn import LinearRegression

# --- Simulated Training Data ---
np.random.seed(42)
X = np.random.rand(200, 100)  # 200 samples, 100 CpG sites
y = np.random.randint(20, 70, size=200)  # Simulated biological ages

# --- Preprocessing ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Train Concrete ML Model ---
model = LinearRegression()
model.fit(X_scaled, y)

# --- Save Model & Scaler ---
MODEL_DIR = "fhe_biological_age_model"
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_DIR, "model.joblib"))
joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.joblib"))

print("✅ Model and scaler saved successfully to 'fhe_biological_age_model/'")

