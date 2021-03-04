from models import app, db, User
from flask import jsonify, request, redirect, url_for

@app.route('/')
def home():
    return jsonify(message="Welcome to my api")

@app.route('/users', methods=['GET', 'POST'])
def user_index_create():
    if request.method == "GET":
        # get all users in db
        users = User.query.all()
        if len(users) > 0:
            print(type(users[0]))
            results = [user.to_dict() for user in users]
            return jsonify(results)
        else:
            return 'no users found'
    
    if request.method == "POST":
        new_user = User(name=request.form['name'], email=request.form['email'], bio=request.form['bio'])
        db.session.add(new_user)
        db.session.commit()
        print(new_user)
        return jsonify(new_user.to_dict())

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)