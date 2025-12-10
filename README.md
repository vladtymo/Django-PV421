# 🧔💈 Barbershop Website
### Overview

This project is a full-stack web application for managing a barbershop.
It provides admin tools for maintaining barbers and services, and a customer-facing interface for booking appointments and leaving feedback.

## ✨ Features

### **Admin / Management**
- **Barbers CRUD**
  - Create new barbers
  - Edit barber details
  - Delete or deactivate barbers
  - View list of all barbers

- **Services CRUD**
  - Create services (e.g., haircut, shave, grooming)
  - Define service price and duration
  - Update service information
  - Delete or archive services

### **Client / User**
- **Service Booking**
  - Choose a barber
  - Select a service
  - Pick a date and time
  - Submit a booking request
  - Receive booking confirmation

- **Feedback System**
  - Leave a review after the appointment
  - Rate barbers and services
  - View past feedback for transparency


## 🏃‍♂️ How to Run the Django App

### 1. Install Dependencies
Make sure you have **Python 3.10+** and **pip** installed.

#### Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate     # Linux / macOS
.venv\Scripts\activate        # Windows
```

#### Install required packages:
```bash
pip install -r requirements.txt
```

#### Run the Development Server
```bash
python manage.py runserver
```
