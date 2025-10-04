# 📧 SpamHam Detector (Django + Machine Learning)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

A **web-based spam/ham message classification system** built using **Django** and **Machine Learning (Naive Bayes, Logistic Regression, SVM)**.  
This project provides a modern web UI where you can:
- Classify messages as **Spam** or **Ham**
- Compare predictions across multiple ML models
- View a **dashboard** with all past classifications
- Use it as a **production-ready monitoring tool**

---

## 🚀 Features

✅ Classify messages instantly as Spam or Ham  
✅ Choose between multiple ML models (Naive Bayes, Logistic Regression, SVM)  
✅ Dashboard to track and filter historical predictions  
✅ Responsive and modern UI  
✅ Built with production best practices (modular code, database logging, model persistence)  

---

## 📂 Project Structure

SpamHamApplication/
│── detector/ # Main Django app
│ ├── migrations/
│ ├── static/ # Static files (CSS/JS)
│ ├── templates/detector/ # HTML templates
│ ├── models.py # MessageLog DB model
│ ├── views.py # Business logic
│ ├── urls.py # App routes
│ └── train_models.py # ML training script
│
│── ml_models/ # Saved ML models (.joblib)
│── SpamHamApplication/ # Django project settings
│── manage.py
│── requirements.txt
│── README.md
└── .gitignore


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/SpamHamDetector.git
cd SpamHamDetector

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train ML models
python detector/train_models.py

5️⃣ Run migrations
python manage.py migrate

6️⃣ Start the server
python manage.py runserver

7️⃣ Access the app

👉 Open browser: http://127.0.0.1:8000/detector/classify/
👉 Dashboard: http://127.0.0.1:8000/detector/dashboard/

📊 Dashboard Preview

The dashboard provides insights into past messages with predictions from all models.

📸 [Insert Screenshot Here]

🧠 Machine Learning Models Used

Naive Bayes → Lightweight & fast, great baseline for text classification

Logistic Regression → More robust linear classifier

Support Vector Machine (SVM) → Higher accuracy but heavier on computation

🔒 Security & Production Notes

Use PostgreSQL/MySQL instead of SQLite for real deployments

Add authentication for dashboard access

Enable HTTPS & CSRF protection in production

Deploy via Docker / Gunicorn / Nginx for scaling

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (dev), PostgreSQL (prod-ready)

ML Models: scikit-learn (joblib serialization)

🤝 Contributing

Fork the repo 🍴

Create a feature branch (git checkout -b feature-new)

Commit changes (git commit -m "Added new feature")

Push to branch (git push origin feature-new)

Open a Pull Request 🚀

📜 License

This project is licensed under the MIT License – feel free to use it for personal or commercial projects.

👨‍💻 Author

Gaurav Bagul – AI Developer & Data Scientist
🔗 LinkedIn
 | 🔗 GitHub


---

⚡ This README is **ready-to-go** — looks professional, clear, and attractive for recruiters or collaborators.  

Do you want me to also **generate badges for test coverage, code quality (Codacy/SonarQube), and deployment (Heroku/Azure)** so it looks even more like a real-world SaaS project?
