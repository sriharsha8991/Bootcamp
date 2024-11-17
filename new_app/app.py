from flask import Flask

# Initialising your Flask applciation
app = Flask(__name__)

# Defining Route

@app.route("/")
def home(): #view Function
    return "<h1>Helloooo</h1>"

@app.route("/home")
def mainpage():
    return "this is a home Page"

if __name__ == "__main__": # start the application if and only if it executed
    app.run(debug=True)