from flask import render_template, request, redirect, url_for

from models import User

def register_routes(app,db):

    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method=='GET':
            users=User.query.all()
            return render_template('index.html',users=users)
        elif request.method=='POST':
            name=request.form['name']
            email=request.form['email']

            new_user=User(name=name,email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/delete/<int:user_id>', methods=['POST'])
    def delete_user(user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        return redirect(url_for('index'))