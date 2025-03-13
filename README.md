# Inventory Management System

A Django-based inventory management system with Django Rest Framework (DRF) API support.

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip package manager

### Installation
1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/inventory-system.git
   cd inventory-system

2. **Create virtual environment**
   ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
   
3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
   
4. **Database setup**
   ```bash
    python manage.py migrate
   
5. **Create superuser**
   ```bash
    python manage.py createsuperuser

### Running the Project
**Start development server**

    python manage.py runserver
    
**Access endpoints**

Admin Panel: http://localhost:8000/admin/

Inventory List: http://localhost:8000/inventory/

API Endpoint: http://localhost:8000/api/inventory/

Item Detail: http://localhost:8000/inventory/1/


**Testing**
Run test suite:

    python manage.py test inventory

**Static Files Management**
Placeholder images should be stored in:

inventory/static/inventory/images/

**For production:**

    python manage.py collectstatic

