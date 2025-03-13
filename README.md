# Inventory Management System

A Django-based inventory management system with Django Rest Framework (DRF) API support.

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip package manager

### Installation
1. **Clone repository**
   ```bash
   git clone https://github.com/suwakanda/inventory-system.git
   
2. **Create virtual environment**
   ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
   
3. **Install Django Rest Framework (DRF)：**
   ```bash
   pip install djangorestframework django-filter
   
4. **Database setup**
   ```bash
   cd inventory-system
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

Item Detail: http://localhost:8000/inventory/(item id)/


**Testing**
Run test suite:

      python manage.py test inventory

**Static Files Management**
Placeholder images should be stored in:

inventory/static/inventory/images/

**For production:**
   ```bash
    python manage.py collectstatic

