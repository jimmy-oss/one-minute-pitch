from flask import Flask,render_template

# create an instance of my app
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

     
     

# application endpoints
# create my decorator -> route
@app.route('/')
@app.route("/home")
def home ():
       return render_template('home.html',posts=posts)

@app.route("/about")
def about ():
       return render_template("about.html")
  
  
     
if __name__== '__main__':
    app.run(debug=True)