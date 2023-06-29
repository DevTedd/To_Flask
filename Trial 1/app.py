from flask import Flask

app = Flask(__name__)


#Defining the home page of our site
@app.route("/") # this sets the route to this page
def home():
    return "<b><i>Hello!</b></i><br> this is the main page <h1>HELLO</h1>" #using basic html inline



if __name__ == "__main__":
    app.run()
