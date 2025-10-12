# 🧠 Gender & Race Predictor

An interactive **Streamlit web application** that predicts a person’s **gender** and **race (or country of origin)** based on either their **name** or a **facial image**.  
This project combines simple machine learning and computer vision models to provide **quick, intuitive predictions** through a friendly interface.

---

## 🚀 Features

- ✅ Predict **gender and nationality** from a given **name**  
- ✅ Predict **gender and race** from an uploaded **face image**  
- ✅ Beautiful, responsive **Streamlit UI**  
- ✅ Displays **country flags** for name-based predictions  
- ✅ Emoji-enhanced, easy-to-read results  

---

## 🧩 Project Structure

Gender_Race_Predictor/
│
├── app.py # Main Streamlit app (UI)
├── image_predictor.py # Face-based prediction using DeepFace
├── name_predictor.py # Name-based prediction using names_dataset
└── utils.py # Utility functions and emojis for display


---

## 🧰 Installation

Install dependencies (preferably inside a virtual environment):

pip install streamlit deepface names-dataset countryflag pillow


> 💡 **Note:**  
> DeepFace requires a deep learning backend such as **TensorFlow** or **PyTorch**.  
> Install TensorFlow with:  
> ```
> pip install tensorflow
> ```  
> or follow installation instructions from [PyTorch](https://pytorch.org/get-started/locally/).

---

## ⚙️ How to Run

git clone https://github.com/yourusername/gender-race-predictor.git
cd gender-race-predictor
streamlit run app.py


Open your browser at [http://localhost:8501](http://localhost:8501) to view the app.

---

## 🖥️ Usage

### 👤 Name Prediction

1. Select **Name** mode.  
2. Enter a first name (e.g., `Ali`, `Sophia`, `Hiroshi`).  
3. View the predicted **gender** and **country of origin**.  
4. A **country flag** appears next to the result if available.

### 🖼️ Image Prediction

1. Select **Image** mode.  
2. Upload a portrait photo (`.jpg`, `.jpeg`, `.png`).  
3. **DeepFace** analyzes the face and predicts **gender** and **dominant race**.  
4. View prediction alongside the uploaded image.

---

## 📦 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app. Shows title, banner, mode selector. Calls `process_name_input()` or `process_image_input()`. |
| `name_predictor.py` | Uses `names_dataset` to predict gender & country. Retrieves flags with `countryflag`. |
| `image_predictor.py` | Uses `DeepFace` to predict gender & race from an image. Handles temporary file storage and display. |
| `utils.py` | Emoji constants & `display_prediction()` function for formatted Streamlit output. |

---

## 🧠 Technologies Used

| Library | Purpose |
|---------|---------|
| **Streamlit** | Build web interface |
| **DeepFace** | Face analysis (gender & race) |
| **names_dataset** | Predict gender & nationality by name |
| **countryflag** | Display country flags dynamically |
| **Pillow (PIL)** | Image processing and handling |

---

## ⚠️ Ethical Disclaimer

This project is for **educational and demonstration purposes only**.  
Predictions are **probabilistic** and may be **inaccurate**.  
Do not use this system for decisions affecting people’s **rights, privacy, or opportunities**.  

> ⚠️ Models may reflect **biases** in their training data. Always use responsibly.

---

## 🪄 Example Outputs

| Mode  | Input         | Output |
|-------|---------------|--------|
| Name  | `Emily`       | 🧬 **Female** 🇺🇸 **United States** |
| Image | Portrait photo | 🧬 **Male** 🌍 **Middle Eastern** |

---


💡 **Tip:** GitHub automatically renders Markdown beautifully — no extra formatting needed.

