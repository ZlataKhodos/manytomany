from flask import Flask, render_template

from dao import db
from dao.db import PostgresDb
from dao.orm.model import Child

app = Flask(__name__)

db = PostgresDb()

@app.route('/')
def hello_world():
    result1 = db.sqlalchemy_session.query(Child).all()
    result2 = db.sqlalchemy_session.query(Child).all()
    return render_template('parenttochild.html', children=result1, parents=result2)


if __name__ == '__main__':
    app.run()
