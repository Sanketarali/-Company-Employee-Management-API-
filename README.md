# Company and Employee Management API

This Django REST API facilitates the management of companies and their employees, supporting CRUD operations and providing endpoints to retrieve employees for specific companies. It is designed for easy integration and efficient data handling.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [License](#license)

## Features
- Create, read, update, and delete companies and employees.
- Retrieve a list of employees for a specific company.
- Simple and intuitive API endpoints for easy integration.

## Technologies Used
- **Django**: A high-level Python Web framework.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **SQLite/PostgreSQL/MySQL**: Databases for storing company and employee data (configurable).
- **Python**: Programming language used for the backend.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- A database (SQLite, PostgreSQL, or MySQL)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required packages:**
   ```bash
    pip install -r requirements.txt

4. **Set up the database:**
   ```bash
   Update the settings.py file with your database configuration.
   Run migrations:
   python manage.py migrate

5. **Create a superuser (optional for accessing the admin site):**
   ```bash
   python manage.py createsuperuser

6. **Run the server:**
   ```bash
   python manage.py runserver

7. **Now, your API should be running at http://127.0.0.1:8000/.**

**API Endpoints**
Companies
List Companies<br>
GET /companies/<br>
Create Company<br>
POST /companies/<br>
Retrieve Company<br>
GET /companies/{id}/<br>
Update Company<br>
PUT /companies/{id}/<br>
Delete Company<br>
DELETE /companies/{id}/<br>


**Employees**
List Employees<br>
GET /employees/<br>
Create Employee<br>
POST /employees/<br>
Retrieve Employee<br>
GET /employees/{id}/<br>
Update Employee<br>
PUT /employees/{id}/<br>
Delete Employee<br>
DELETE /employees/{id}/<br>
Company Employees<br>
List Employees of a Specific Company<br>
GET /companies/{companyId}/employees/<br>








