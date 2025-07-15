Budget Tracker API

//what it entails//

A simple but powerful Django REST API that lets users track categories and expenses.  
Built with Django + Django REST Framework.  
Secured with JWT. Tested with Postman

Features

//features//

WT authentication (login, refresh)
Add and manage budget categories
Create and list expenses per user
Auth-protected endpoints
Fully testable via Postman

Tech Stack

///tech stack///

- Python 3
- Django
- Django REST Framework
- SimpleJWT
- Pipenv

///created user///
python manage.py createsuperuser

Authentication

///authentication//

We use JWT (JSON Web Tokens) for authentication.
Get token:
POST /api/token/
Payload:
///
json
{
  "username": "your_username",
  "password": "your_password"
}
/////
Refresh token:
http server
POST /api/token/refresh/
Payload:


