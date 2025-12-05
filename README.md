# 📝 Task Manager Django Project

A **Django-based Task Manager** application to manage **workers**, **tasks**, and **positions** with authentication, search, and CRUD functionality.

---

## 🚀 Features

- **User Management**
  - 👤 Custom Worker model (extends Django User)
  - 🔑 Login and Add new Worker
- **Worker Management**
  - ➕ Add, ✏️ update, 🗑 delete workers
  - 🎯 Assign positions
  - 🔍 Search by username
- **Task Management**
  - ➕ Create, ✏️ update, 🗑 delete tasks
  - 👥 Assign tasks to multiple workers
  - ⏰ Track deadlines, priorities, and task types
  - ✅ Mark tasks as completed
- **Position Management**
  - ➕ Add, ✏️ update, 🗑 delete positions
- **Responsive UI**
  - Built with Django templates + Free template Gradient Able

---

## 🛠 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## 📂 Project Structure

```
task_manger/
├── task_manager/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── templatetags
│   ├── tests
│   ├── urls.py
│   └── views.py
├── templates/
├── static/
├── manage.py
├── db.sqlite3
├── README.md
```

## ✅ Testing

Run all tests:
```bash
python manage.py test
```

 **Includes tests for:**
- Worker forms and validation
- Task forms and validation
- Views: listing, creating, updating, deleting
- Search functionality
