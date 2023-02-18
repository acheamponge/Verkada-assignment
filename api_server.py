import flask
from flask import Flask, render_template, request, url_for, jsonify
import requests 
import os 
from requests.exceptions import Timeout

app = flask.Flask(__name__)
app.config["DEBUG"] = True

command = ''
data = ''


WEB_CLIENT_ENDPOINT = "http://127.0.0.1:5000/logs"
os.environ['NO_PROXY'] = '127.0.0.1:5000/logs'

@app.route('/stream', methods=['GET'])
def virtual_camera():
    global command
    return command
    
@app.route('/post', methods=['POST'])
def post_logs():
    global data
    global command
    input_json = request.get_json(force=True)
    #print('data from client:', input_json)
    data = input_json
    res=requests.post(url = WEB_CLIENT_ENDPOINT , json=data) 
    #print('response from web client:',res.text)
    command = ''
    return ("API server received logs")
    

@app.route('/', methods=['GET','POST'])
def commands():
    global data
    
    global command
    
    if (request.remote_addr) == '127.0.0.1':
        command = 'get_logs'
        return 'API Server received get_logs command'
    
    



    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
