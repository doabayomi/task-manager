# Backend directory
Backend codebase for task manager project


## File Structure
| File/Directory | Function                                      |
|----------------|-----------------------------------------------|
| `app.py`       | Flask app file                                |
| `users/`       | User and authentication-related functionality |
| `resources/`   | Modules for tasks, teams, projects, etc.      |
| `pages/`       | Module for static pages and error pages       |
| `models/`      | Database models                               |
| `static/`      | Frontend components and resources             |
| `templates/`   | Web pages for the Flask application           |
| `config.py`    | Config script for environmental variables     |

## Installation
* Create your own virtual environment
```bash
python3 -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

  NOTE: If you are using windows before running `activate` run this line:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

* Set up the js libraries in the `/static` and `/templates` directory
```bash
npm install
```


* Create your own `.env` file with the following variable names:
  | Field                    | Description                              |
  |--------------------------|------------------------------------------|
  | `DATABASE_URI`           | The URI of the database for `SQLAlchemy` |
  | `SECRET_KEY`             | The secret key for `sqlite` usage        |
  | `SECURITY_PASSWORD_SALT` | The salt for encryption for passwords    |

  You can run the app using `flask run`.

## API
### Authentication Routes
* `/auth/login`
* `/auth/register`
* `/auth/logout`
* `/auth/profile`

# Linting HTML
```bash
npx linthtml 'yourfile.html'
```