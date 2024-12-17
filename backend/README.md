# Backend directory
Backend codebase for task manager project


## File Structure
| File/Directory | Function       |
|----------------|----------------|
| `app.py`       | Flask app file |

## Usage
For development:
* Create your own `.env` file with the following variable names:
    | Field          | Description                              |
    |----------------|------------------------------------------|
    | `DATABASE_URI` | The URI of the database for `SQLAlchemy` |
    | `SECRET_KEY`   | The secret key for `sqlite` usage        |