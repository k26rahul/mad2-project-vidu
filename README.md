# Household Services Application - V2

A multi-user platform for comprehensive home services, connecting customers with verified service professionals.

Project submission for Modern Application Development II (January 2025).

> **Note:** This repository contains only the prototype version (used to learn and experiment with concepts) of the Household Services Application. Development in this repository was left incomplete, and the actual project development was moved to [this separate repository](https://github.com/vidhatrihr/mad2-project).

## Features

- Admin Dashboard: Manage users, services, and approvals.
- Service Professionals: Accept/reject service requests.
- Customers: Search, book, and review services.
- Secure authentication (RBAC).
- Backend jobs for notifications and reports.
- Optimized performance with caching.

## Folder Structure

```
├── backend/
│   ├── app.py               # Flask application entry point
│   ├── models.py            # Database models
│   ├── populate_db.py       # Database seeding script
│   └── routes/
│       ├── admin.py         # Admin routes
│       ├── auth.py          # Authentication routes
│       ├── customer.py      # Customer routes
│       └── professionals.py # Professional routes
│
└── frontend/
    ├── src/
    │   ├── components/    # Reusable Vue components
    │   ├── views/
    │   │   ├── admin/     # Admin dashboard views
    │   │   ├── auth/      # Login/Register views
    │   │   ├── customer/  # Customer dashboard views
    │   │   └── professionals/ # Professional dashboard views
    │   ├── App.vue        # Root component
    │   ├── main.js        # Application entry point
    │   ├── router.js      # Vue router configuration
    │   └── store.js       # State management
    └── index.html         # HTML entry point
```

## Tech Stack

- **Backend:** Flask, Flask-CORS, Flask-SQLAlchemy
- **Frontend:** Vue.js, Bootstrap
- **Database:** SQLite
- **Caching & Jobs:** Redis, Celery

## Setup

### Backend Setup

```sh
# Clone repo
git clone https://github.com/k26rahul/mad2-project-vidu.git
cd mad2-project-vidu

# Setup virtual environment
python -m venv venv
source venv/bin/activate # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python backend/app.py
```

### Frontend Setup

```sh
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at:

- Frontend: http://localhost:5173
- Backend API: http://localhost:5000
