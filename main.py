from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for flash messages

# Database configuration (SQLite file)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define Task model (table)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False, unique=True)  # prevent duplicates
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # NEW
    priority = db.Column(db.String(10), default="Medium")  # NEW (Low, Medium, High)

@app.get("/")
def home():
    # Order by: incomplete first, then by priority, then newest
    tasks = Task.query.order_by(Task.completed.asc(), Task.priority.desc(), Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)

@app.post("/add")
def add_task():
    task_content = request.form.get("task")
    priority = request.form.get("priority", "Medium")

    if not task_content.strip():
        flash("Task cannot be empty!")
        return redirect(url_for("home"))

    # Check for duplicate
    if Task.query.filter_by(content=task_content).first():
        flash("Task already exists!")
        return redirect(url_for("home"))

    new_task = Task(content=task_content, priority=priority)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.post("/toggle/<int:task_id>")
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("home"))

@app.post("/edit/<int:task_id>")
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_content = request.form.get("new_content")
    new_priority = request.form.get("new_priority")

    if not new_content.strip():
        flash("Task cannot be empty!")
        return redirect(url_for("home"))

    task.content = new_content
    task.priority = new_priority
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
