# 📊 SmartDash – Your All-in-One Productivity Dashboard

SmartDash is a comprehensive web-based productivity platform built with Django that brings together inspiration, organization, and focus in one clean, accessible space. Smartdash is built with the purpose to simplify  your digital life.

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [🛠️ Technology Stack](#️-technology-stack)
* [📸 Screenshots](#-screenshots)
* [🚀 Installation & Setup](#-installation--setup)
* [🧪 Usage](#-usage)
* [🌐 Deployment](#-deployment)
* [📄 License](#-license)

---

## ✨ Features

* 🧠 Daily motivation and quotes widget
* ✅ Task manager with deadlines and priorities
* 📅 Calendar overview and scheduling
* 🕒 Pomodoro timer for focused work
* 🌙 Dark and light theme support
* 🔒 User authentication with profile customization

---

## 🛠️ Technology Stack

| Layer    | Technology                        |
| -------- | --------------------------------- |
| Backend  | Django 5.2.4                      |
| Frontend | HTML5, CSS3, JavaScript           |
| Database | SQLite (for development)          |
| Auth     | Django built-in authentication    |
| Styling  | Custom CSS with responsive design |

---

## 📸 Screenshots

### 🏠 Dashboard Overview

### ✅ Task Manager

### 📅 Calendar & Events

### 👤 User Profile

---

## 🚀 Installation & Setup

Follow these steps to get SmartDash running locally:

```bash
# 1. Clone the repository
git clone https://github.com/Adelodunpeter25/smartdash
cd smartdash

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Run database migrations
python manage.py migrate

# 5. (Optional) Create a superuser for admin access
python manage.py createsuperuser

# 6. Launch the development server
python manage.py runserver
```

Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧪 Usage

* Log in or sign up to access your personalized dashboard.
* Add, edit, or remove tasks with ease.
* Use the Pomodoro timer to stay focused.
* Track daily goals and events using the calendar widget.
* Switch themes based on your preference.

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
