"""
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
@app.route('/receive-data',methods=['POST'])
def receive_data():
    data = request.get_json()

    print("received data:", data)
    #return "data Received"
    return json.dumps({'message': 'Data received successfully'})


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)
"""

from flask import Flask, request,jsonify, send_file
from flask_cors import CORS
import json
import pyttsx3
import os
app = Flask(__name__)
CORS(app)
#hello = None for vewrsion 6 chrometohtml
hello = ""
engine = pyttsx3.init()
@app.route('/receive-data',methods=['POST'])
def receive_data():
    data = request.get_json()
    global hello
    if hello:
        hello = ""
    for i in range(len(data)):
        hello += "line"
        hello += f"{i+1}"
        if data[i]["i"].isspace():
            hello+="space"
        else:
            hello+= data[i]["i"]
    #hello = data[0]['textContent'] # this is for version 6 chrometo html

    print("received data:", data)
    #return "data Received"
    return json.dumps({'message': 'Data received successfully'})



@app.route("/send-mp3",methods=['GET'])

def send_mp3():
    if os.path.exists("speech.mp3"):
        os.remove("speech.mp3")
    engine.setProperty("rate",145)
    
    engine.save_to_file(hello, "speech.mp3")
    engine.runAndWait()
    
    
   
    mp3_filename = "speech.mp3"
    return send_file(mp3_filename,mimetype= "audio/mpeg")

@app.route('/send-data',methods= ['GET'])

def send_data():
    data = {hello: "data sent from flask server"}
    return jsonify(data)
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)