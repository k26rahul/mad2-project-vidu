# Household Services Application - V2

A multi-user platform for comprehensive home services, connecting customers with verified service professionals.

## Features

- Admin Dashboard: Manage users, services, and approvals.
- Service Professionals: Accept/reject service requests.
- Customers: Search, book, and review services.
- Secure authentication (RBAC).
- Backend jobs for notifications and reports.
- Optimized performance with caching.

## Tech Stack

- **Backend:** Flask, Flask-CORS, Flask-SQLAlchemy
- **Frontend:** Vue.js, Bootstrap
- **Database:** SQLite
- **Caching & Jobs:** Redis, Celery

## Setup

```sh
# Clone repo
git clone https://github.com/vidhatrihr/mad2-project.git
cd mad2-project

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
