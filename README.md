# AI-Based Intelligent Fitness System

## Project Overview
The AI-Based Intelligent Fitness System is a web application that provides **personalized fitness recommendations** based on user inputs such as age, weight, height, and fitness goals. The system leverages **AI/ML algorithms** to suggest workout plans, diet plans, and general fitness tips.

---

## Features
- User registration and login
- Input personal metrics: age, weight, height, fitness goal
- AI-driven workout and diet recommendations
- Track fitness progress (optional extension)
- User-friendly web interface with HTML templates
- Extensible to mobile apps via REST API

---

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite/MySQL (optional)
- **AI/ML:** scikit-learn, pandas, numpy
- **Data Visualization:** matplotlib/plotly
- **Others:** pickle for model serialization

---

## Project Structure

AI_Fitness_Recommendation/
│
├── README.md
├── requirements.txt
├── app.py # Main Flask application
├── model/
│ ├── fitness_model.pkl # Pre-trained ML model
│ └── preprocess.py # Model training script
├── templates/
│ ├── index.html
│ ├── register.html
│ └── recommendations.html
├── static/
│ ├── css/style.css
│ ├── js/script.js
│ └── images/logo.png
├── data/
│ └── fitness_data.csv # Sample dataset for training
├── docs/
│ └── Project_Documentation.pdf
└── utils/
└── recommendation.py # Recommendation engine logic


---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd AI_Fitness_Recommendation


Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Run the application

python app.py


Access the app
Open a web browser and go to: http://127.0.0.1:5000/
