import os, time
from flask import Flask, jsonify, request

import photohash

from handlers import HashProcessor

PORT = 8080
HOST = 'localhost'

app = Flask(__name__)

@app.route("/")
def handleDefault():
  return "Hello World I am running on " + str(PORT)

@app.route("/getHash", methods=['POST'])
def handleGetHash():
  HashWorker = HashProcessor.HashProcessor()

  file=request.files['file']

  if file:
    filePath = os.path.join('./resources/', file.filename)
    file.save(filePath)

    start = time.clock()
    
    hashOne = HashWorker.getHash(filePath)
    #hashTwo = HashWorker.getHash('./resources/riskhappy.jpg')
    hashValue = HashWorker.getHashValue(hashOne)
    #hashValueTwo = HashWorker.getHashValue(hashTwo)

    end = time.clock()
    print("Time to hash: %i" % (end - start) )

    payload = {
      'hash': hashOne,
      'hashValue': hashValue,
      #'hashTwo': hashTwo,
      #'hashValueTwo': hashValueTwo,
      #'distance': HashWorker.getHashDistance(hashOne, hashTwo)
    }

    return jsonify(**payload)
  return "OOPS"

if __name__  == "__main__":
  app.run(host='0.0.0.0', port=PORT)
  print("Start serving at port %i" % PORT)
