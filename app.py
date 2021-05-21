#Required imports
import os
from flask import Flask,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from firebase_admin import credentials, firestore, initialize_app
import requests
import json
#Initialize Flask app
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    
#     def __repr__(self):
#         return'<Task %r>' % self.id
@app.route("/Data",methods=["POST"])
def Data():
    if request.method=="POST":
        dis_id = request.form.get("dis_id",False)
        print(request.form.to_dict())
    firebase = requests.get('https://owasp-test-855b8-default-rtdb.firebaseio.com/Data.json', None)
    print(dis_id)
    jsonData = json.loads(firebase.text)
    jsonData1 = json.dumps(jsonData)
    html = []
    for i in jsonData.keys():
        html.append(jsonData[i]["Discord"])
    print(html)
    if dis_id in html:
        return "exists"
    else:
        return "not exists"
    return html

#Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/secondpage")
def secondpage():
    return render_template('secondpage.html')

@app.route("/landingpage")
def landingpage():
    return render_template('landingpage.html')

if __name__ == "__main__":
    app.run(debug=True)