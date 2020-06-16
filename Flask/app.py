from flask import Flask  #, url_for,redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(9), nullable=False)
	value = db.Column(db.Integer, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return "<Tasks %r>" % self.id

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/event')
def index():
    return render_template('index.html')

@app.route('/value')
def values():
    return render_template('value.html')

if __name__=='__main__':
    app.debug=True
    app.run()