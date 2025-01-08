# Task Manager App
ALX porfolio webstack project


## File Structure
| File/Directory | Function                                        |
|----------------|-------------------------------------------------|
| `app.py`       | Flask app file                                  |
| `users/`       | User and authentication-related functionality   |
| `resources/`   | Modules for tasks, teams, projects, etc.        |
| `pages/`       | Module for static pages and error pages         |
| `models/`      | Database models                                 |
| `static/`      | Frontend components and resources               |
| `templates/`   | Web pages for the Flask application             |
| `config.py`    | Config script for environmental variables       |
| `schemas/`     | Validation schemas for resources in application |

## Installation
* Create your own virtual environment
```bash
python3 -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

  NOTE: If you are using windows before running the `activate` script run this line:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

* Set up the js libraries in the `/static` and `/templates` directory
```bash
npm install
```

* To lint HTML files you can use this command
```bash
npx linthtml 'yourfile.html'
```

* Create your own `.env` file with the following variable names:
  | Field                    | Description                              |
  |--------------------------|------------------------------------------|
  | `DATABASE_URI`           | The URI of the database for `SQLAlchemy` |
  | `SECRET_KEY`             | The secret key for `sqlite` usage        |
  | `SECURITY_PASSWORD_SALT` | The salt for encryption for passwords    |

* You can then run the app using `flask run`.

## API
### Authentication Endpoints
**POST `/auth/login`**: Logs in a user
```json
// Sample request
{
  "email": "user@email.com",
  "password": "Somepassword2"
}

// Sample response body, 200
{
  "message": "Login successful"
}

// Header Response
// Set-Cookie: Cookie: session=.eJwljkF.......gXcw; HttpOnly ...
```
**POST `/auth/register`**: Registers a new user
```json
// Sample request
{
  "email": "user@email.com",
  "password": "Somepassword2"
}

// Sample response body, 200
{
  "message": "User created",
  "email": "user@email.com"
}
```

**POST `/auth/logout`**: Logs out an authenticated user
```json
// Sample response body, 200
{
  "message": "Logout successful"
}
```

**POST `/auth/profile`**: Updates an authenticated user's profile
```json
// Sample request
{
  "email": "user@email.com",
  "password": "Somepassword1",
  "new_password": "Newpassword2"
}

// Sample response body, 200
{
  "message": "Profile successfully updated"
}
```

**GET `/auth/profile`**: Gets an authenticated user's profile
```json
// Sample response body, 200
{
  "email": "user@email.com"
}
```

### Task Endpoints
**POST `/tasks`**: Creates a new task for the authenticated user

```json
// Sample request
{
  "name": "Write Documentation",
  "description": "Document the API in README.md",
  "status": "to do",
  "priority": "normal",
  "deadline": "2025-01-31T12:00:00"
}

// Sample response, 201 status code
{
  "id": 1,
  "name": "Write Documentation",
  "description": "Document the API in README.md",
  "status": "to do",
  "priority": "normal",
  "deadline": "2025-01-31T12:00:00",
  "date_added": "2025-01-07T14:00:00",
  "user_id": 1
}
```

**GET `/tasks`** OR **GET `/tasks/<task_id>`**: Retrieves all tasks for the authenticated user or a particular task based on id
```json
// Sample response to GET /tasks, 200 status code
[
  {
    "id": 1,
    "name": "Write Documentation",
    "description": "Document the API in README.md",
    "status": "to do",
    "priority": "normal",
    "deadline": "2025-01-31T12:00:00",
    "date_added": "2025-01-07T14:00:00",
    "user_id": 1
  },
  ...
]

// Sample response to GET /tasks/1. 200 status code
{
  "id": 1,
  "name": "Write Documentation",
  "description": "Document the API in README.md",
  ...
  "user_id": 1
}
```

**PUT `/tasks/<task_id>`**: Updates a task for the user
```json
// Sample request
{
  "name": "Updated Task Name",
  "status": "in progress"
}

// Sample response, 200
{
  "message": "Task updated successfully."
}
```

**DELETE `/tasks/<task_id>`**: Deletes a task for the authenticated user.

```json
// Sample success response 200
{
  "message": "Task deleted successfully."
}
```

#### Status codes
| Code                          | Meaning                                                                  |
|-------------------------------|--------------------------------------------------------------------------|
| **200 OK**                    | Request succeeded.                                                       |
| **201 Created**               | Resource created successfully.                                           |
| **400 Bad Request**           | Invalid request data. (usually with error message showing what is wrong) |
| **401 Unauthorized**          | Authentication required. (would try to redirect to login page)           |
| **404 Not Found**             | Resource not found.                                                      |
| **500 Internal Server Error** | Server error.                                                            |