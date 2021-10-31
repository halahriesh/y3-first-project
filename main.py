from flask import Flask, jsonify, request, render_template, url_for,redirect
import random
from database import *

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/',methods=['GET','POST'])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    username=request.form["username"]
    if username==None :
      return render_template("login.html")
    else :
      add_user(username)
      return redirect(url_for("home", user=username))
  return render_template('login.html')
  if request.method =="POST":
    username = request.form['username']
    users = session.query(Users).all()






@app.route('/in/<string:user>',methods=['GET','POST'])
def home(user):
  if request.method =="GET":
    return render_template('in.html', username=user)
  else :
    name=request.form["name"] 
    review=request.form["review"]
    if name or review == None :
      return render_template ("in.html")
    else:
      add_review(name,review)
      return redirect(url_for("in.html", name=name, review=review))

  return render_template("in.html")
    


@app.route('/reviews/<string:name>/<string:review>',methods=['GET','POST'])
def reviews(name,review):
  if request.method=="GET":
    return render_template("reviews.html",name = name ,  review= review )

  return render_template('reviews.html')


@app.route("/fornow")
def forno():
  return render_template("reviews.html")

@app.route("/hoho")
def hoho():
  return render_template("in.html")


@app.route("/koko")
def koko():
  return render_template("quotes.html")


@app.route('/quote',methods=['GET','POST'])
def quotes():
  if method.request=="GET":
   return ('quotes.html')

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(9000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)
