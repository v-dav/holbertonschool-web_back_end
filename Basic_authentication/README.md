# HTTP Basic Authentication
![Python](https://img.shields.io/badge/Python-3.7-blue?style=for-the-badge&logo=python&logoColor=white)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-blue?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

<p align="center">
  <img src="https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/69bafc22-f51b-4d20-b099-50a27da6d01b" alt="Description de l'image">
</p>

## 🧐 Project Overview

Welcome to the "Basic Authentication" project! This project explores the authentication process and guides you through implementing Basic Authentication on a simple API. While it's essential to note that, in a real-world scenario, you'd typically use established modules or frameworks (such as Flask-HTTPAuth in Python-Flask) for this purpose, this project provides a hands-on experience to comprehend each step of the authentication mechanism.

## ⚙️ Project Description

The "Basic Authentication" project introduces you to the fundamentals of authentication and the steps involved in implementing Basic Authentication. Throughout the project, you will gain insights into key concepts such as:

1. **Authentication Basics:**
   - Understand the significance of authentication in securing APIs.
   - Explore different authentication mechanisms and their role in protecting sensitive data.

2. **Base64 Encoding:**
   - Learn what Base64 encoding is and its relevance in the authentication process.
   - Explore how to encode a string in Base64, a fundamental step in Basic Authentication.

3. **HTTP Header Authorization:**
   - Understand the role of the Authorization header in the HTTP request.
   - Explore how Basic Authentication leverages the Authorization header for secure communication.

4. **Flask Framework:**
   - Familiarize yourself with Flask, a web framework for Python.
   - Implement Basic Authentication within the Flask framework for a practical understanding.

## 📖 Learning Objectives

Upon completing this project, you should be able to explain the following concepts without relying on external resources:

- Define the concept of authentication and its role in securing APIs.
- Understand Base64 encoding and its application in the authentication process.
- Encode a string in Base64 to enhance data security.
- Recognize the importance of the Authorization header in HTTP requests.
- Implement Basic Authentication within the Flask framework.

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


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
