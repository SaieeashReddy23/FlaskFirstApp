from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable = False)
    marks = db.Column(db.Integer)

    def __init__(self,id,name,marks):
        self.id = id
        self.name=name
        self.marks=marks

    def __str__(self):
        return "{id : %d , name : %s , marks : %d }" % (self.id,self.name,self.marks)
        


@app.route("/",methods = ['POST','GET'])
def index():
    return jsonify({"data":"Hello world"})


@app.route("/home/<int:num>",methods = ["GET"])
def square(num):
    return jsonify({"squared" : num**2})


@app.route("/add",methods={"POST"})
def addContent():
    data = request.get_json()
    print(data)

    todoData = Todo(data["id"],data["name"],data["marks"])

    print(todoData)

    try:
        db.session.add(todoData)
        db.session.commit()
    except:
        return "There was an issue adding to db"


    return jsonify({"id":data["id"],"name":data["name"],"marks":data["marks"]})


@app.route("/get")
def getContent():
    st = Todo.query.all()
    all_students = [{"id":std.id,"name" : std.name,"marks":std.marks}  for std in st]
    return  jsonify( all_students) 

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
