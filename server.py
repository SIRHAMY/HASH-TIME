import os
from flask import Flask, request

PORT = 8080
HOST = 'localhost'

app = Flask(__name__)

@app.route("/")
def handleDefault():
  return "Hello World I am running on " + str(PORT)

@app.route("/getHash")
def handleGetHash():

  return "Calculating hash..."

if __name__  == "__main__":
  app.run(host='0.0.0.0', port=PORT)
  print("Start serving at port %i" % PORT)
