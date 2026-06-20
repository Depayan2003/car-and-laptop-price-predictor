# 🚀 Car & Laptop Price Prediction App

A machine learning-powered web application built with **Streamlit** that predicts:

* 💻 Laptop Prices
* 🚗 Car Prices

The application combines multiple trained machine learning models into a single interactive interface where users can enter product specifications and receive instant price predictions.

---

## 📌 Features

### 💻 Laptop Price Prediction

Predicts laptop prices based on specifications such as:

* Brand and model attributes
* Storage configuration (SSD, HDD, Flash Storage, Hybrid)
* Screen resolution
* Touchscreen support
* IPS display
* Retina display
* 4K display support
* Other hardware-related features

### 🚗 Car Price Prediction

Predicts car prices using:

* Years used
* Kilometers driven
* Vehicle rating
* Condition score
* Mileage (km/l)
* Top speed
* Horsepower
* Torque

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Machine Learning

* Scikit-Learn
* TensorFlow / Keras
* NumPy
* Pandas
* Joblib

### Programming Language

* Python

---

## 📂 Project Structure

```text
car-and-laptop-price-predictor/
│
├── app.py
├── car_price_model.keras
├── price_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/car-and-laptop-price-predictor.git
cd car-and-laptop-price-predictor
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📊 Machine Learning Models

### Laptop Model

* Scikit-Learn Pipeline
* Saved using Joblib (`price_model.pkl`)
* Performs preprocessing and prediction in a single pipeline

### Car Model

* Deep Neural Network
* Built using TensorFlow/Keras
* Saved in Keras format (`car_price_model.keras`)

Architecture:

```text
Input Layer (8 Features)
        ↓
Normalization Layer
        ↓
Dense(256, ReLU)
        ↓
Dense(128, ReLU)
        ↓
Dense(64, ReLU)
        ↓
Dense(32, ReLU)
        ↓
Dense(1)
```

---

## 📈 Future Improvements

* Add model performance metrics
* Deploy on Streamlit Cloud
* Improve UI/UX
* Add additional vehicle and laptop features
* Integrate database support
* Add prediction history

---

## 👨‍💻 Author

**Depayan Debnath**

* GitHub: https://github.com/Depayan2003
* LinkedIn: https://linkedin.com/in/depayan-debnath

---

## 📺 Live Demo
* https://car-and-laptop-price-predictor.streamlit.app *

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
