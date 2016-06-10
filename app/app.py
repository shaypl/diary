from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello <br> this is an events diary"
@app.route("/<action>,<day>,<month>,<year>,<title>,<description>")
def dataInput(action,day,month,year,title,description):
    return action+" "+day+" "+month+" "+year+" "+title+" "+description

if __name__ == "__main__":
    app.run(debug=True)
