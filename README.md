# Hotel Reservation System

A RESTful Hotel Reservation System built with **Django REST Framework**, featuring OTP-based authentication, JWT tokens, and a fully documented API via Swagger.

---

## ✨ Features

- 🏨 **Hotel Reservation System** — manage hotels, rooms, and bookings
- 🔐 **Authentication with OTP** — login & register using One-Time Passwords
- ⚡ **Redis-backed OTP storage** — fast and temporary OTP storage with automatic expiry
- 🎟️ **JWT Authentication** — secure token-based authentication for users
- 👤 **Custom User Model** — a personalized `User` model tailored to the project's needs
- 📖 **Swagger API Documentation** — interactive API docs for testing and exploring endpoints
- 🛠️ **Built with Django REST Framework** — clean, scalable, and modular API design

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| Django | Web framework |
| Django REST Framework | API development |
| Redis | OTP storage |
| JWT (SimpleJWT) | Token-based authentication |
| drf-yasg / drf-spectacular | Swagger API documentation |
| SQLite / PostgreSQL | Database |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd hotel-reservation
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
REDIS_HOST=redis://127.0.0.1:6379/1
```

### 5. Run Redis

Make sure Redis is running locally:

```bash
redis-server
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server and create admin user

```bash
python manage.py createsuperuser
python manage.py runserver
```

---

## 📖 API Documentation

Once the server is running, access the Swagger UI at:

```
http://127.0.0.1:8000/swagger/
```

---

## 🔑 Authentication Flow

1. **Register / Login** → user submits phone number (or email)
2. **OTP generated** → stored in Redis with a short TTL
3. **User verifies OTP** → receives a **JWT access & refresh token**
4. **Authorized requests** → include the token in the `Authorization: Bearer <token>` header

---

## 📁 Project Structure

```
hotel-reservation/
├── accounts/          # Custom User model, OTP, JWT auth
├── hotels/            # Hotel & room management
├── reservation/      # Booking logic
├── main/            # Project settings & URLs
├── requirements.txt
└── manage.py
```


