from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ci491_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, index=True)
    names = db.Column(db.String, index=True)
    emails = db.Column(db.String, index=True)
    phones = db.Column(db.String)

db.create_all()

@app.route("/")
def index():
    users = User.query
    return render_template('results.html', title='Senior Design Project',
                           users=users)

if __name__ == '__main__':
    app.run()