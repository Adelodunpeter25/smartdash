# 📊 SmartDash – Your All-in-One Productivity Dashboard

**SmartDash** is a clean, responsive, web-based productivity platform built with Django. It’s designed to unify your essential tools—like notes, conversions, quotes, and calculations—into one seamless dashboard, keeping students and professionals organized and focused.

---

## 📚 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [📸 Screenshots](#-screenshots)
- [🚀 Installation & Setup](#-installation--setup)
- [🌐 Deployment](#-deployment)
- [📄 License](#-license)

---

## ✨ Features

- 🧠 Daily motivational quote generator for a focused start
- 📝 Notepad for quick notes, drafts, or journals (with autosave and edit options)
- 💰 Currency converter using real-time exchange rates
- 📐 Unit converter supporting length, weight, temperature, speed, volume, and time
- ➗ Simple arithmetic calculator for quick math operations
- 🎯 Organized, distraction-free dashboard tailored for students and professionals

---

## 🛠️ Technology Stack

| Layer       | Technology                     |
|------------ |-------------------------------|
| Backend     | Django 5.2.4                   |
| Frontend    | HTML5, CSS3, JavaScript        |
| Database    | SQLite (default)               |
| Auth        | Django built-in authentication |
| Styling     | Custom CSS (fully responsive)  |

---

## 📸 Screenshots

> Add images to your `screenshots/` folder and link them below.

### 🏠 Dashboard Overview

![Dashboard](screenshots/dashboard.png)

### ✅ Task Manager

![Tasks](screenshots/tasks.png)

### 📝 Notepad

![Notepad](screenshots/notepad.png)

### 💱 Currency & Unit Converter

![Converter](screenshots/converter.png)

---

## 🚀 Installation & Setup

Follow these steps to run SmartDash locally:

```bash
# 1. Clone the repository
git clone https://github.com/Adelodunpeter25/smartdash
cd smartdash

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. (Optional) Create admin account
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver


Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---
## 🌐 Deployment

SmartDash can be deployed on platforms like **Render**, **Heroku**, or **VPS**. For production:

* Configure a production-ready database (e.g. PostgreSQL).
* Set your environment variables (e.g. `SECRET_KEY`, `DEBUG`, etc.).
* Use Gunicorn or another WSGI server.
* Collect static files with:

```bash
python manage.py collectstatic
```

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for full details.

---

**SmartDash** – Simplify your digital workflow and boost your productivity 🚀
