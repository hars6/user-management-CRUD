# User Management API Project(Django + MySQL)

A simple backend service built using **Django** and **MySQL**, providing basic **CRUD operations** for user management.  

---

## 🚀 Features
- Create User  
- Get All Users  
- Get Single User  
- Update User  
- Delete User 

---

## 🛠 Tech Stack
- **Python** (Django Framework)
- **MySQL** Database
- **Postman** (for API testing)

---

## 📂 Folder Structure

```
user_api_project/
│   manage.py
│
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── users/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

---

## ⚙️ Setup Instructions

Follow these steps to run this project on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/hars6/user-management-CRUD
cd user_api_project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django mysqlclient
```

### 4. Create MySQL Database
Open MySQL Workbench and run:

```sql
CREATE DATABASE user_api_db;
```

### 5. Configure Database in Django
Open:
```
backend/settings.py
```

Update:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user_api_db',
        'USER': 'root',
        'PASSWORD': '' 
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoints

### ➤ Create User  
**POST** `/api/users/create/`  
**Body:**
```json
{
  "name": "Harsh Panchal",
  "email": "harsh@gmail.com",
  "age": 25
}
```

### ➤ Get All Users  
**GET** `/api/users/`

### ➤ Get Single User  
**GET** `/api/users/<id>/`

### ➤ Update User  
**PUT** `/api/users/update/<id>/`  
**Body:**
```json
{
  "name": "Updated User",
  "email": "updated@gmail.com",
  "age": 30
}
```

### ➤ Delete User  
**DELETE** `/api/users/delete/<id>/`

---
