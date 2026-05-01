# 🚀 Team Task Manager (Django Full-Stack)

A full-stack web application to manage team projects, assign tasks, and track progress with role-based access (Admin / Member).

---

## 🌐 Live Demo

🔗 https://web-production-a8bb4.up.railway.app/login/

---

## 📌 Project Overview

This application allows teams to:

* Create and manage projects
* Add team members to projects
* Assign tasks to members
* Track task status (Pending → In Progress → Done)
* View dashboard with task insights

It is built using **Django + Django REST Framework + MySQL/PostgreSQL + Tailwind CSS** and deployed on Railway.

---

## 🎯 Key Features

### 🔐 Authentication

* User Signup & Login
* JWT-based authentication
* Secure password handling

### 👥 Role-Based Access

* **Admin**

  * Create projects
  * Add members
  * Assign tasks
  * View all tasks

* **Member**

  * View assigned tasks
  * Update task status

---

### 📁 Project Management

* Create projects
* Add/remove team members
* View project list

---

### ✅ Task Management

* Create tasks
* Assign tasks to users
* Track status:

  * Pending
  * In Progress
  * Done

---

### 📊 Dashboard

* View all tasks
* Status tracking
* Overdue detection (optional)

---

## 🛠️ Tech Stack

### Backend

* Django
* Django REST Framework
* PostgreSQL (Railway DB)
* Gunicorn

### Frontend

* HTML
* Tailwind CSS
* JavaScript (Fetch API)

### Deployment

* Railway (Cloud Hosting)

---

## ⚙️ Project Structure

```
core/
│
├── accounts/      # Authentication & user profile
├── projects/      # Project management
├── tasks/         # Task handling
│
├── templates/     # HTML pages
├── core/          # Settings, URLs
├── manage.py
├── requirements.txt
├── Procfile
```

---

## 🚀 Installation (Local Setup)

### 1. Clone repo

```bash
git clone https://github.com/your-username/core.git
cd core
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start server

```bash
python manage.py runserver
```

---

## 🌐 Deployment (Railway)

* Connected GitHub repo
* Added PostgreSQL database
* Configured `DATABASE_URL`
* Used Gunicorn for production server
* Added Pre-deploy commands:

```bash
python manage.py migrate && python manage.py collectstatic --noinput
```

---

## 📦 API Endpoints (Sample)

| Method | Endpoint                | Description    |
| ------ | ----------------------- | -------------- |
| POST   | /api/auth/signup/       | Register user  |
| POST   | /api/auth/login/        | Login          |
| GET    | /api/projects/my/       | Get projects   |
| POST   | /api/projects/create/   | Create project |
| POST   | /api/tasks/create/      | Create task    |
| PUT    | /api/tasks/{id}/update/ | Update task    |

---

## 🔐 Role Logic

* Admin → Full control
* Member → Limited to assigned tasks

---

## 🧠 Challenges Faced

* Deployment issues with Railway
* Database configuration (PostgreSQL)
* Role-based UI rendering
* API authentication handling

---

## 📈 Future Improvements

* Kanban Board (Drag & Drop)
* Notifications system
* Email alerts
* Analytics dashboard
* Mobile responsiveness improvements

---

## 👨‍💻 Author

**Chakri**

* GitHub: https://github.com/chakri31383

---

## ⭐ Conclusion

This project demonstrates:

* Full-stack development skills
* API design & integration
* Role-based access control
* Real-world deployment

---

⭐ If you like this project, give it a star!
