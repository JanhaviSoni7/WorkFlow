from flask import Flask  #module, class

app = Flask(__name__)  #obj of class Flask

@app.route("/")  #path after the domain name
def hello_world():
  return "Hello, World!"
