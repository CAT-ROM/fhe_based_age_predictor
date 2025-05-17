# 🧬 FHE-Based Biological Age and Aging Pace Estimator

This is my submission to [Zama AI's Bounty #143](https://github.com/zama-ai/bounty-program/issues/143):  
**"Implement an FHE-based Biological Age and Aging Pace Estimation ML Model Using Zama Libraries."**

I developed a Fully Homomorphic Encryption (FHE) pipeline using [Concrete ML](https://github.com/zama-ai/concrete-ml) to estimate **biological age** from DNA methylation data. The model supports encrypted input prediction and is deployed with a real-time Gradio interface on Hugging Face Spaces.

---

## 🚀 Live Demo

👉 [Click here to try the live app on Hugging Face](https://huggingface.co/spaces/CAT-ROM/fhe-biological-age-predictor)

You can input 100 CpG methylation values and receive an encrypted, privacy-preserving biological age estimate instantly.

---

## 📌 Project Summary

Biological age reflects the actual physiological condition of cells rather than the number of years since birth (chronological age). This project estimates biological age using DNA methylation data — specifically 100 CpG beta values.

The model is trained using `concrete-ml`'s `LinearRegression`, compiled with FHE, and executed securely using `fhe="execute"`. It ensures:
- **Data privacy** during inference
- **Deployability** through Hugging Face Spaces
- **Scientific relevance** with a basis in epigenetic clocks

---

## 💡 Why Biological Age?

Recent studies suggest that **genetics explain only 15–25% of the aging process**. Environmental factors, stress, and lifestyle play a significant role.

This project is inspired by:

- **Horvath Clock**: DNA methylation age of human tissues
- **DunedinPACE**: Measures the pace of aging
- **Levine, Chen, Sehgal Clocks**: Biomarkers for lifespan, healthspan, and system-specific aging

---

## 🔐 Why FHE?

**Fully Homomorphic Encryption (FHE)** allows computation directly on encrypted data. In this app:
- Input beta values are encrypted
- Model inference is performed without decryption
- Predictions are decrypted after execution

This is ideal for **genomic and medical data privacy**.

---

## 🛠️ How It Works

| Step | Description |
|------|-------------|
| 🧬 Input | 100 CpG methylation beta values (comma-separated, range 0–1) |
| ⚖️ Preprocessing | Normalized using `StandardScaler` |
| 🧠 Model | `LinearRegression` from Concrete ML |
| 🔐 Inference | `fhe="execute"` mode on compiled model |
| 🌐 Interface | Gradio app deployed on Hugging Face |

---

## 📂 File Structure

