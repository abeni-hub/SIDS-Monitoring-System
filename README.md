# SIDS Monitoring System 🍼💡  

This is my **Final Year Project**: a **Sudden Infant Death Syndrome (SIDS) Monitoring System**.  
It is designed to **record infant health status** using real-time sensors and **predict potential risks** using a machine learning model.  

The system provides **real-time monitoring**, **risk prediction**, and **alerting capabilities** to help caregivers take quick action.  

---

## 🔎 Description  
- The system uses **Raspberry Pi** to collect data from sensors monitoring infant conditions.  
- The backend is built with **Django REST Framework**, providing APIs for data storage and prediction.  
- The frontend is developed with **React**, offering a user-friendly dashboard to view infant status in real-time.  
- A **Logistic Regression Machine Learning Model** is integrated to predict whether an infant is at risk based on sensor readings.  
- **My contribution / gap filled**: I integrated a **GSM Module** with the Raspberry Pi to **automatically make a phone call to the caregiver** when the infant is predicted to be at risk.  

---

## ⚙️ Features  
- Real-time infant monitoring with Raspberry Pi sensors  
- Machine learning–based **risk prediction** (Logistic Regression)  
- REST APIs for data communication (Django REST Framework)  
- Modern frontend with **React**  
- Alerts and notifications for caregivers via **GSM call**  
- Data logging for analysis  

---

## 🛠️ Tech Stack  
- **Hardware:** Raspberry Pi + Sensors (temperature, heartbeat, etc.) + GSM Module  
- **Backend:** Django REST Framework (API)  
- **Frontend:** React  
- **Machine Learning:** Logistic Regression (risk prediction model)  
- **Database:** SQLite / PostgreSQL  

---

## 🚀 Installation & Setup  

### 1. Clone the Repository  
```bash
git clone <REPO_URL>
cd SIDS-Monitoring-System
### 2. Backend Setup (Django REST Framework)
cd backend
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs at: http://127.0.0.1:8000

3. Frontend Setup (React)
cd frontend
npm install
npm start

```
Frontend runs at: http://localhost:3000

### 4. Raspberry Pi Setup

Connect sensors (temperature, heartbeat, etc.) to Raspberry Pi

Connect and configure the GSM Module for caregiver calls

Run the Python script to collect sensor readings and send them to the Django API

API

###📊 Machine Learning Model

The system uses a Logistic Regression model trained on infant health data.

It predicts whether the infant is at risk or not at risk of SIDS.

Predictions are displayed on the React dashboard in real time.

If at risk, the system triggers a GSM call to notify the caregiver immediately.

🖼️ System Architecture
flowchart TD
    A[Infant Sensors\n(Heartbeat, Temp, etc.)] --> B[Raspberry Pi]
    B --> C[Django REST API\n(Backend)]
    C --> D[Database\n(SQLite/PostgreSQL)]
    C --> E[ML Model\n(Logistic Regression)]
    C --> F[React Dashboard\n(Web Frontend)]
    B --> G[GSM Module\n(Calls Caregiver if at risk)]
**📬 Contact**

LinkedIn: Abenezer Sileshi

Gmail: abinesilew@gmail.com

Telegram: @Aben14i
