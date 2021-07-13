from application import app, db
from application.models import Tasks


@app.route('/add/<task_name>')
def add(task_name):
    new_task = Tasks(name=task_name)
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"
