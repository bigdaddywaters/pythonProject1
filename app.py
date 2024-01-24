from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TOdo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/about')
def index():
    return "https://bbk12e1-cdn.myschoolcdn.com/ftpimages/1058/user/large_user_6869111_322.jpg?crop=0,0,100%,85%&resize=200,200"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    new_todo =


    app.run(debug=True)



