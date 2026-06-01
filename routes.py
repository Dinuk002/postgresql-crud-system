from flask import render_template,request

from models import User

def register_routes(app,db):

    @app.route('/')
    def index():
        users=User.query.all()
        return render_template('index.html',users=users)