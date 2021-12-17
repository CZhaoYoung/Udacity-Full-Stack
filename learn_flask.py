from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# build connection from flask to sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9817@localhost:5432/postgres'
db = SQLAlchemy(app)


# by inheriting from db.Model
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # able to customize a printable string (useful for debugging)
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

# Detects models and creates tables for them (if they don't exist)
db.create_all()


# a decorator that takes an input function index() as the callback that get
# invoked when a request to route / comes in from a client.
@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello! ' + person.name


if __name__ == '__main__':
    app.run()