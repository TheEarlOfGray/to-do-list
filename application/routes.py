from werkzeug.utils import redirect
from application import app, db
from application.models import Tasks, AddForm
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_task = Tasks(name=form.name.data, desc=form.desc.data)
        db.session.add(new_task)
        db.session.commit()
        items = Tasks.query.all()
        return render_template('view_all.html', message="Task Added!", items=items)
    else:
        return render_template('add_task.html', form=form)

@app.route('/view_all')
def view_all():
    items = Tasks.query.all()
    return render_template('view_all.html', items=items)

@app.route('/delete/<int:task>')
def delete(task):
    item = Tasks.query.get(task)
    db.session.delete(item)
    db.session.commit()
    return redirect('/view_all')

