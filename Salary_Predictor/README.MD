# 💰 Salary Predictor Web App

A simple Machine Learning web application that predicts salary based on years of experience. Built using Python, trained with Scikit-learn, and deployed using Streamlit inside Docker.



## 🚀 Features

* Predict salary based on experience
* Displays:

  * Annual salary (₹)
  * Salary in LPA (Lakhs Per Annum)
  * Monthly salary
* Clean and interactive UI using Streamlit
* Docker-based environment for easy setup



## 🧠 Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Docker



## 📁 Project Structure

Salary_Predictor/
│
├── app.py          # Streamlit web app
├── train.py        # Model training script
├── salary.csv      # Dataset
├── model.pkl       # Trained model (generated)
├── README.md


## 📊 Dataset

The dataset contains the following fields:

* Name
* Age
* Gender
* Education
* Experience (used for model)
* Job Role
* City
* Salary

👉 Currently, the model uses only **Experience** for prediction (basic version).


## ⚙️ How to Run (Docker)

### 1. Pull Python Image

docker pull python:3.13

### 2. Run Container

docker run -it -p 8501:8501 -v D:/Project:/app python:3.10 bash


> Replace `D:/Project` with your actual project path.



### 3. Install Dependencies

Inside container:

pip install pandas scikit-learn streamlit


### 4. Train Model

cd /app/Salary_Predictor
python train.py

This will create:

model.pkl

### 5. Run Web App

streamlit run app.py --server.address 0.0.0.0 --server.port 8501


## 🌐 Access App

Open in browser:

http://localhost:8501



## 📸 Output

* Enter years of experience
* Click "Predict Salary"
* View:

  * 💰 Salary in INR
  * 📊 Salary in LPA
  * 📅 Monthly Salary

---

## ⚠️ Notes

* Make sure `model.pkl` is generated before running the app
* Docker container resets packages unless using Dockerfile


