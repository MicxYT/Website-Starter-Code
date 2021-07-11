from flask import Flask # import flask

app = Flask(__name__) # define app as flask

@app.route("/") # our route eg: example.com/
def home():
    return "This Is The Homepage" # return text

@app.route("/help") # our route eg: example.com/help
def help():
    return "This is the help page" # return text

app.run(host="0.0.0.0",port="80") # Run the website
