from flask import Flask,render_template,request,url_for,redirect,render_template
import csv
import hack
app = Flask(__name__)
def write_to_csv(data):
    with open("password_list.csv","a")as file:
        email=data["email"]
        password=data["password"]
        writer=csv.writer(file)
        writer.writerow([email,password])
def write(data):
    with open("email_list.csv","a")as file:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        writer=csv.writer(file)
        writer.writerow([email,subject, message])

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/<page_name>')
def name(page_name):
    return render_template(page_name)
@app.route('/submit_form', methods=["POST","GET"])
def submit_form():
    if request.method=="POST":
        data= request.form.to_dict("message")
        write(data)
        return redirect("thank_you.html")
    return "somthing went wronge"
@app.route('/submit', methods=["POST","GET"])
def submit():
    if request.method=="POST":
        data= request.form.to_dict("message")
        write_to_csv(data)
        x=hack.main(data["password"])
        print(x)
        return render_template("answer.html",res=x)
    return "somthing went wronge"
