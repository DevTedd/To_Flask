from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


#Defining the home page of our site
@app.route("/blank") # this sets the route to this page
def home2():
    return "<b><h2> Hello! this is the main page </h2></b> <h1>HELLO</h1>" #using basic html inline

#This is another page created by modifiying the url, by replacing the name in the url with the one included on the page


#@app.route("/admin") #can name 2 function the same
#def admin():
 #   return redirect(url_for("home"))

@app.route("/admin")
def admin():
    return redirect(url_for("user", name='Admin!'))
# Now we when we go to /admin we will redirect to user with the argument "Admin!"

#Rendering templates 
@app.route("/")
def home():
    return render_template("index2.html")

#creating anohter home page based on using python calls
@app.route("/test")
def test():
    return render_template("index.html", content="Testing")

@app.route("/test_func")
def funcs():
    return render_template("index3")

if __name__ == "__main__":
    app.run()
