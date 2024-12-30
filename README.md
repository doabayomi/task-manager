# Backend directory
Backend codebase for task manager project


## File Structure
| File/Directory | Function                                |
|----------------|-----------------------------------------|
| `app.py`       | Flask app file                          |
| `auth/`        | Module for authentication               |
| `pages/`       | Module for static pages and error pages |
| `models/`      | Module for db models                    |

## Usage
For development:
* Create your own virtual environment
```bash
python3 -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

  NOTE: If you are using windows before running  `activate` run this line:


```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

* Create your own `.env` file with the following variable names:
    | Field                     | Description                              |
    |---------------------------|------------------------------------------|
    | `DATABASE_URI`            | The URI of the database for `SQLAlchemy` |
    | `SECRET_KEY`              | The secret key for `sqlite` usage        |
    | ` SECURITY_PASSWORD_SALT` | The salt for encryption for passwords    |

    You can run the app using `flask run`.
    NOTE: It is advisable to use a virtual environment for developing your project.

## API
### Authentication Routes
* `/auth/login`
* `/auth/register`
* `/auth/logout`
* `/auth/profile`