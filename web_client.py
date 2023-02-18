import requests   
import os
from flask import Flask, render_template, request, url_for, jsonify
from requests.exceptions import Timeout


#API Server end point
API_ENDPOINT = "http://127.0.0.1:8080"
os.environ['NO_PROXY'] = '127.0.0.1:8080'




app = Flask(__name__)
app.config["DEBUG"] = True

data = {}


    
@app.route('/logs', methods=['GET','POST'])
def get_logs():
    global API_ENDPOINT
    global data
 
    try:
        r = requests.get(url = API_ENDPOINT, timeout=30)
        
    except Timeout as ex:
        print("Exception Raised: ",ex)
        
    if request.method == 'POST':
        input_json = request.get_json(force=True)
        data = input_json  
    return data
   
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
