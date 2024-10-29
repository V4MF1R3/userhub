# UserHub

UserHub is a Django-based user management application with features for user registration, login, profile management, password reset, and change functionalities, making it ideal for securely handling user data and authentication.

Demonstration video: [https://youtu.be/JM6UTyW377E](https://youtu.be/JM6UTyW377E)

## Features
* **User Registration:** New users can sign up by providing a username, email, and password.
* **User Login:** Authenticated users can log in using their credentials.
* **Password Management:** Includes password reset via email, and in-app password change options.
* **User Profile:** Users can view their profile details, including email and date joined.
* **Dashboard:** Simple dashboard for logged-in users.
* **Email Integration:** Password reset emails are sent through Mailtrap for development/testing.

## Setup

### Prerequisites
* Python 3.7+
* Django 4+
* A Mailtrap account for email testing (optional for production)

### Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/your-username/UserHub.git
    cd UserHub
    ```
2. Create a Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Update the `EMAIL_BACKEND` and related email settings directly in `settings.py`:
    1. Open `UserHub/settings.py`.
    2. Scroll to the email configuration section and set it up as follows (replace placeholders with your actual credentials):
        ```bash
        # Email settings
        EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
        EMAIL_HOST = "sandbox.smtp.mailtrap.io"  # sandbox.smtp.mailtrap.io is for testing, use smtp.mailtrap.io for production.
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_USER = "your_mailtrap_username"
        EMAIL_HOST_PASSWORD = "your_mailtrap_password"
        ```
    3. Save the changes in 'settings.py'.
5. Apply Migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the Development Server:
    ```bash
    python manage.py runserver
    ```
7. Access the Application: Open `http://127.0.0.1:8000` in your browser.

## Important URLs
* Login: `/login/`
* Signup: `/signup/`
* Forgot Password: `/forgot-password/`
* Profile: `/profile/`
* Dashboard: `/dashboard/`

## Usage
* **User Registration:** New users can sign up using their email and password.
* **Login:** Users can log in and access the dashboard.
* **Password Reset:** Users can reset their password through the "Forgot Password" link, which sends an email with a reset link.
* **Change Password:** Logged-in users can update their password from the profile settings.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
Thanks to Django for its robust framework and to Mailtrap for easy email testing.