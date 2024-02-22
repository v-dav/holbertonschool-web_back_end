# HTTP Session Authentication
![Python](https://img.shields.io/badge/Python-3.7-blue?style=for-the-badge&logo=python&logoColor=white)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-blue?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

<p align="center">
  <img src="https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/f09eef05-ff04-4eae-b39e-3229f1b2a2b8" alt="Description de l'image">
</p>

## 🧐 Project Overview

In the Session Authentication project, we will explore the authentication process and guide you through implementing Basic Authentication on a simple API. While it's essential to note that, in a real-world scenario, you'd typically use established modules or frameworks (such as Flask-HTTPAuth in Python-Flask) for this purpose, this project provides a hands-on experience to comprehend each step of the session authentication mechanism.

## 📖 Learning Objectives

Upon completing this project, you should be able to explain the following concepts without relying on external resources:

- Explain the concept of session-based authentication.
- Implement session management in a web application.
- Understand the role of session cookies in maintaining user state.
- Enhance the security of user sessions through best practices.
- Handle user authentication and authorization using sessions.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users' endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


##  🙇 Author

[Vladimir Davidov](https://github.com/v-dav) - Holberton School
