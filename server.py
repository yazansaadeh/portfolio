from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)
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
        print(data)
        return redirect("thank_you.html")
    return "somthing went wronge"
