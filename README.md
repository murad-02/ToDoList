# Flask ToDo List

A simple, modern ToDo List web app built with Flask, SQLAlchemy, and SQLite.  
Features a stylish UI with theme toggle, persistent tasks in the database, and basic CRUD operations.

## Features

- Add, complete, and delete tasks
- Tasks are stored in a SQLite database
- Responsive, animated UI with light/dark theme toggle
- Uses Flask, Flask-SQLAlchemy, and Flask-Migrate

## Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for Python dependencies

## Setup

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the app:**
    ```sh
    python main.py
    ```

3. **Open in browser:**  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
main.py                  # Flask app and database models
requirements.txt         # Python dependencies
templates/
  index.html             # Main HTML template
instance/
  todo.db                # SQLite database (auto-created)
migrations/              # Alembic migration scripts
```

## Usage

- **Add a task:**  
  Enter text in the input and click ➕ or press Enter.
- **Complete a task:**  
  Click the ✓ button next to a task.
- **Delete a task:**  
  Click the 🗑️ button next to a task.
- **Toggle theme:**  
  Click "Toggle Theme" at the top right.

## Database

- Uses SQLite (`todo.db` in `instance/` directory)
- Tasks have fields: `id`, `content`, `created_at`, `completed`

## Migrations

- Database migrations managed with Alembic/Flask-Migrate.
- Migration scripts are in [migrations/versions/](migrations/versions/).

## License

MIT License