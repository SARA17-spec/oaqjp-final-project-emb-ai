from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
  
### run : python server.py
### Visit http://127.0.0.1:5000/ in your browser to check if it's running.
### Open your terminal or command prompt and log in to Heroku: heroku login
### pip freeze > requirements.txt
###  Create a Procfile
### A Procfile tells Heroku how to run your application. Create a new file named Procfile (no file extension) in the root of your project, and add the following content:
### makefile
### Copy code
### web: gunicorn server:app
###Deploy to Heroku
###git init
### git add .
### git commit -m "Initial commit"
###Create a Heroku App : heroku create your-app-name
###Push the Code to Heroku :git push heroku master
###Verify Deployment : heroku open
