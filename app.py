#Required imports
import os
from flask import redirect,Flask,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from firebase_admin import credentials, firestore, initialize_app
import requests
import json
# import pyrebase
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



# Firebase Setup
  # For Firebase JS SDK v7.20.0 and later, measurementId is optional
# firebaseConfig = {
#   "apiKey": "AIzaSyDTT2f-Xbhl4pQeunt51gDefvXt-Wui-AY",
#   "authDomain": "owasp-test-855b8.firebaseapp.com",
#   "databaseURL": "https://owasp-test-855b8-default-rtdb.firebaseio.com",
#   "projectId": "owasp-test-855b8",
#   "storageBucket": "owasp-test-855b8.appspot.com",
#   "messagingSenderId": "591067196689",
#   "appId": "1:591067196689:web:ed7c9e81f84558451ab0b0",
#   "measurementId": "G-8TB6Z07KQ2"
# };
# # firebase.initializeApp(firebaseConfig);
# firebase_storage = pyrebase.initialize_app(firebaseConfig)
# storage = firebase_storage.storage()

@app.route("/Data",methods=["POST"])
def Data():
    if request.method=="POST":
        dis_id = request.form.get("dis_id",False)
        print(request.form.to_dict())
    firebase = requests.get('https://owasp-test-855b8-default-rtdb.firebaseio.com/Certificates.json', None)
    print(dis_id)
    jsonData = json.loads(firebase.text)
    jsonData1 = json.dumps(jsonData)
    html = []
    for i in jsonData.keys():
        xyz=list(jsonData[i].keys())[0]
        year=jsonData[i][xyz]["Year"]
        if jsonData[i][xyz]["Discord"] == dis_id:
            return redirect("https://storage.googleapis.com/owasp-test-855b8.appspot.com/dynamic%20certificate/"+jsonData[i][xyz]["Name"]+"-"+year)
    # print(html)
    # if dis_id in html:
    #     return "exists"
    # else:
    return "not exists"
    # return html

# Downloading certificates
# storage.child("dynamic certificate/Pratham-1990-1999").download("Pratham-1990-1999")


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