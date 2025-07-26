from flask import Flask  #module, class

app = Flask(__name__)  #obj of class Flask


@app.route("/")  #path after the domain name
def hello_world():
  return "Hello, sir!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
