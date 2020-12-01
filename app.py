print("Hello Day UI")
print("Now UI")
print("#############################################################")
from flask import Flask
from datetime import datetime
from flask import render_template
#import re

app = Flask(__name__)


#@app.route("/todaystime")
#def homeoftimehome():
#    return "Hello, Time!"





@app.route("/todaystime/")
@app.route("/todaystime/<name>")
def hello_there(name = None):

    if name == "simple":
        return printoutnow()

    else:
        return render_template(
        "hello_threeReturn.html",
        name=name,
        date=datetime.now()
     

    )
# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/now/")
def now():
    return render_template("now.html")

@app.route("/personal/")
def personal():
    return render_template("now.html")

@app.route("/api/")
def api():
    return render_template("now.html")

def printoutnow():
    now = datetime.now()
    print(now)
    somethingnew = now.__str__()
    return somethingnew



print("http://127.0.0.1:5000/")
print("http://127.0.0.1:5000/about")
print("http://127.0.0.1:5000/contact")

print("#######################################")
print("http://127.0.0.1:5000/todaystime/simple")
print("http://127.0.0.1:5000/todaystime/sammy")
print("http://127.0.0.1:5000/todaystime/raw")
print("http://127.0.0.1:5000/todaystime")


#@app.route("/api/data")
#def get_data():
#    return app.send_static_file("data.json")
app.run()