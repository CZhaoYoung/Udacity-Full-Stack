
# App version 1.1
# Modify the app by using AJAX to send data to flask
# Here, we will use fetch instead on the cline side.
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:9817@localhost:5432/postgres'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


db.create_all()


# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#     description = request.get_json()['description']
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     return jsonify({
#         'description': todo.description
#     })

# Ues sessions in controllers
# try...expect...finally
@app.route('/todos/create', method=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort (400)
    else:
        return jsonify(body)


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
    # return render_template('index.html', data=[
    #     {'description': 'Todo 1'},
    #     {'description': 'Todo 2'},
    #     {'description': 'Todo 3'}
    # ])