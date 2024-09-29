# Django Parent-Teacher Meeting App

This Django-based web application facilitates communication between parents and teachers by providing a platform for managing parent-teacher meetings. The app allows teachers to post notifications about upcoming meetings, and parents can respond by either accepting or declining the invitation.

## Features

- **User Authentication**: Teachers (admin) and parents can log in to the system securely.
- **Notification Management**: Teachers can create and manage meeting notifications, including details such as date, time, and description.
- **Parent Responses**: Parents can view notifications and respond to meeting invites with "Accept" or "Decline."
- **Student Details**: The system shows relevant information like a student’s USN (University Serial Number), attendance, CGPA, internal marks, and semester details.
- **Teacher Dashboard**: A centralized dashboard for teachers to view student responses and manage meeting notifications.
  
## Tech Stack

- **Backend**: Django (Python), SQLite3 (Database)
- **Frontend**: HTML, CSS
- **Version Control**: Git, GitHub

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

git clone https://github.com/your-username/Django-Parent-Teacher-Meeting-App.git
cd Django-Parent-Teacher-Meeting-App

### 2. Create a virtual environment and install dependencies
Create a virtual environment for your project to keep its dependencies isolated.

#### For macOS/Linux:
python -m venv venv
source venv/bin/activate

####  For Windows:
python -m venv venv
venv\Scripts\activate

#### Then install the required dependencies by running:
pip install -r requirements.txt

### 3. Apply migrations and create superuser
#### Apply the database migrations to set up the database schema.
python manage.py migrate

#### Create a superuser (admin account) to access the admin panel:
python manage.py createsuperuser
#### Follow the prompts to set up your username, email, and password.

### 4. Start the development server
Finally, start the Django development server:
python manage.py runserver
Now, visit http://127.0.0.1:8000/ in your browser to see the app running.
