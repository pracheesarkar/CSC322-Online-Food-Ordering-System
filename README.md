# Rolling Dough Food Ordering System

The Rolling Dough Food Ordering System is an online bakery developed as part of the CSC322 project. It offers a comprehensive solution for managing food orders, deliveries, customer interactions, and employee management.

## Features

- **User Authentication**: Register and log in to the system securely.
- **Menu Management**: Chefs can easily edit the menu, add new items, and update prices.
- **Order Placement**: Customers can create and place orders effortlessly through the user-friendly interface.
- **VIP Program**: Reward loyal customers with discounts and special privileges based on their order history.
- **Rating and Feedback**: Users can provide ratings and feedback on their orders, helping improve service quality.
- **Employee Management**: Managers can promote, demote, hire, and fire employees based on performance and customer feedback.
- **Complaint Handling**: Efficiently manage complaints from customers and employees, ensuring prompt resolution.
- **Health Inspection**: Monitor and maintain the restaurant's health standards, with alerts for inspections and rating updates.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3
- Django

### Installing Dependencies

To install the project dependencies, run the following command:


### Running the Server

To run the server locally, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/CSC322-Rolling-Dough-Food-Ordering-System.git
    ```

2. Navigate to the project directory:

    ```bash
    cd CSC322-Rolling-Dough-Food-Ordering-System
    ```

3. Activate the virtual environment:

    ```bash
    source myenv/bin/activate
    ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. If you encounter any issues related to missing dependencies, install them using the following commands:

    ```bash
    pip install django-crispy-forms
    pip install django-allauth
    ```

6. Run the Django server:

    ```bash
    python manage.py runserver
    ```

### Troubleshooting

If you encounter any issues during the setup process, try the following troubleshooting steps:
- **Database Migration Errors**:  If you encounter errors related to database migrations, make sure you have applied all pending migrations using the `python manage.py migrate` command.
- **Environment Setup Issues**: Double-check that your virtual environment is activated before installing dependencies or running the server. Use the command `source myenv/bin/activate` to activate the virtual environment.

7. Once the server is running, open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the site.

8. To access the admin page, go to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with the following credentials:
    - Username: admin
    - Password: password1


