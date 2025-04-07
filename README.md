# 📸 Gallery Management API with User Authentication

This is a Django + Django REST Framework (DRF) project that supports user registration, authentication, and media management. Authenticated users can view users, albums, and photos through a structured REST API.

---

## 🚀 Features

### 🔐 Authentication
- JWT-based authentication for login/logout and protected endpoints
- Custom user model using UUID
- Email verification and password reset supported

### 👥 Users
- **Endpoint:** `GET /api/users/`
- **Fields:**
  - `name`: Full name of the user
  - `username`: Unique username
  - `email`: User email

### 📁 Albums
- **Endpoint:** `GET /api/albums/`
- **Fields:**
  - `id`: Album ID
  - `user`: UUID of the user who owns the album
  - `title`: Title of the album

### 🖼️ Photos
- **Endpoint:** `GET /api/photos/<album_id>/`
- **Fields:**
  - `album`: Album ID the photo belongs to
  - `title`: Title of the photo
  - `image`: URL of the uploaded image

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv env
source env/bin/activate
pip install -r requirements.txt
