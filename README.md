# GO BETWEEN TRANSPORTATION

Transportation is crucial for enabling communication, trade, and exchange between people, fostering the establishment of civilizations. "GO BETWEEN TRANSPORTATION" aims to streamline transportation logistics and enhance user experience through digitalization and automation.

## Overview

The system focuses on managing transportation requests efficiently, integrating various modes of transport, and ensuring safety and security for users.

## Objectives & Scope

### Objectives

- Enhance safety and security.
- Improve access to facilities.
- Integrate different modes of transport effectively.
- Apply information technology to the transportation business.

### Scope

- User-friendly system accessible to non-technical users.
- Upgradeable for future enhancements.
- Ensures speed, accuracy, and an intuitive GUI.

## Goals

- Implement IT solutions in transportation.
- Provide a secure, user-friendly system for companies, drivers, and users.
- Ensure system security and prevent unauthorized access.
- Automate calculations to eliminate errors.
- Maintain relevant master tables for data management.

## Modules

### 1. Administrator

The administrator manages overall system control and performs the following functions:
- Add locations and vehicle types.
- Verify company/driver requests.
- Manage user complaints and feedback.

### 2. Company

Companies handle trip requests and driver assignments:
- Manage company profile details.
- Add, update, and view vehicles.
- Search and request freelance drivers.
- Confirm trip requests and assign drivers.
- Handle driver leave requests and manage payments.

### 3. Drivers

Drivers hired by companies perform the following functions:
- Manage driver profile details.
- Apply for leave and update leave request status.
- View assigned and completed trips.
- Update trip statuses and provide feedback.

### 4. Freelance Drivers

Freelance drivers not hired directly by companies can:
- Manage freelance driver profile details.
- Add, view, and update vehicles.
- Confirm trip and company requests.
- View and update assigned trips and completed trips.
- Provide feedback on services.

### 5. Users

Users booking trips perform the following functions:
- Manage user profile details.
- Search and request trips from companies and drivers.
- View trip details and make payments.
- Send and view complaints and feedback.

## Getting Started with Django

To get started with "GO BETWEEN TRANSPORTATION" using Django, follow these steps:

1. Clone the repository:
   git clone https://github.com/your-username/go-between-transportation.git

2. Navigate into the project directory:
   cd go-between-transportation
   
3. Set up a virtual environment (optional but recommended):
   python -m venv env

4. Activate the virtual environment (Windows):
   env\Scripts\activate
   or (Mac/Linux):
   source env/bin/activate
   
5. Install necessary dependencies

6. Apply migrations:
   python manage.py migrate

7. Create a superuser (admin):
   python manage.py createsuperuser

8. Start the development server:
   python manage.py runserver

9. Open your web browser and navigate to 'http://localhost:8000' to view the application.
  
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the [MIT License](link-to-license).
