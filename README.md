# Task Management API

The Task Management API allows users to manage tasks, categories, and user accounts with functionalities including creating, reading, updating, deleting tasks, user authentication, and password management.

## Base URL
http://127.0.0.1:8000/api/


## Authentication
This API uses token-based authentication. Users must log in to receive a token, which must be included in the headers of subsequent requests.

### Login
- **Endpoint**: `/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "user@example.com",
      "password": "your_password"
  }

- **Response**:
    ```json
    {
        "token": "your_token_here"
    }

### Register
- **Endpoint**: `/register/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "username": "new_user",
        "email": "user@example.com",
        "password": "your_password"
    }
- **Response**:
    ```json
    {
        "id": 1,
        "username": "new_user",
        "email": "user@example.com"
    }

### Logout
- **Endpoint**: `/logout/`
- **Method**: `POST`
- **Headers**:
    Authorization: Token your_token_here
- **Response**: `204 No Content`

### Password Reset Request
- **Endpoint**: `/reset-password/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "email": "user@example.com"
    }
- **Response**:
    ```json
    {
        "message": "If an account with that email exists, a password reset link has been sent."
    }

### Password Reset Confirmation
- **Endpoint**: `/reset-password/{user_id}/{token}/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "password": "new_password"
    }
- **Response**:
    ```json
    {
        "message": "Password has been reset."
    }

## Task Management Endpoints
### List All Tasks
- **Endpoint**: `/tasks/`
- **Method**: `GET`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Description for Task 1",
            "due_date": "2024-09-30T00:00:00Z",
            "priority": "High",
            "status": "Pending",
            "category": null,
            "recurrence": "None"
        }
    ]

### Create a New Task
- **Endpoint**: `/tasks/`
- **Method**: `POST`
- **Headers**:
    Authorization: Token your_token_here
- **Request Body**:
    ```json
    {
        "title": "New Task",
        "description": "Description for New Task",
        "due_date": "2024-09-30T00:00:00Z",
        "priority": "Medium",
        "status": "Pending",
        "category": null,
        "recurrence": "None"
    }
- **Response**:
    ```json
    {
        "id": 2,
        "title": "New Task",
        "description": "Description for New Task",
        "due_date": "2024-09-30T00:00:00Z",
        "priority": "Medium",
        "status": "Pending",
        "category": null,
        "recurrence": "None"
    }

### Retrieve a Specific Task
- **Endpoint**: `/tasks/{id}/`
- **Method**: `GET`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description for Task 1",
        "due_date": "2024-09-30T00:00:00Z",
        "priority": "High",
        "status": "Pending",
        "category": null,
        "recurrence": "None"
    }

### Update a Specific Task
- **Endpoint**: `/tasks/{id}/`
- **Method**: `PUT`
- **Headers**:
Authorization: Token your_token_here
- **Request Body**:
    ```json
    {
        "title": "Updated Task",
        "description": "Updated description",
        "due_date": "2024-10-01T00:00:00Z",
        "priority": "Low",
        "status": "Pending",
        "category": null,
        "recurrence": "None"
    }
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Updated Task",
        "description": "Updated description",
        "due_date": "2024-10-01T00:00:00Z",
        "priority": "Low",
        "status": "Pending",
        "category": null,
        "recurrence": "None"
    }

### Delete a Specific Task
- **Endpoint**: `/tasks/{id}/`
- **Method**: `DELETE`
- **Headers**:
Authorization: Token your_token_here
- **Response**: `204 No Content`

### Mark a Task as Complete
- **Endpoint**: `/tasks/{id}/complete/`
- **Method**: `POST`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    {
        "status": "task marked as complete"
    }

### Mark a Task as Incomplete
- **Endpoint**: `/tasks/{id}/incomplete/`
- **Method**: `POST`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    {
        "status": "task marked as incomplete"
    }

## Category Management Endpoints
### List All Categories
- **Endpoint**: `/categories/`
- **Method**: `GET`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    [
        {
            "id": 1,
            "name": "Work"
        }
    ]

### Create a New Category
- **Endpoint**: `/categories/`
- **Method**: `POST`
- **Headers**:
Authorization: Token your_token_here
- **Request Body**:
    ```json
    {
        "name": "Personal"
    }
- **Response**:
    ```json
    {
        "id": 2,
        "name": "Personal"
    }

### Retrieve a Specific Category
- **Endpoint**: `/categories/{id}/`
- **Method**: `GET`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Work"
    }

### Update a Specific Category
- **Endpoint**: `/categories/{id}/`
- **Method**: `PUT`
- **Headers**:
Authorization: Token your_token_here
- **Request Body**:
    ```json
    {
        "name": "Updated Category"
    }
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Updated Category"
    }

### Delete a Specific Category
- **Endpoint**: `/categories/{id}/`
- **Method**: `DELETE`
- **Headers**:
Authorization: Token your_token_here
- **Response**: `204 No Content`

## Task History Endpoints
### List Task History
- **Endpoint**: `/history/`
- **Method**: `GET`
- **Headers**:
Authorization: Token your_token_here
- **Response**:
    ```json
    [
        {
            "id": 1,
            "task": 1,
            "status": "Completed",
            "changed_at": "2024-09-20T00:00:00Z"
        }
    ]
