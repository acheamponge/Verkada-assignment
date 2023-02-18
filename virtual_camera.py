import sched, time
from datetime import datetime
import pandas as pd
import random
import logging
import io
import os
import requests 
from requests.exceptions import Timeout
import flask
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True
API_ENDPOINT = "http://127.0.0.1:8080/stream"
API_ENDPOINT_POST = "http://127.0.0.1:8080/post"
os.environ['NO_PROXY'] = '127.0.0.1:8080'

logging.basicConfig(level = logging.INFO)
stream = io.StringIO()
log = logging.getLogger()
handler = logging.StreamHandler(stream)
log.addHandler(handler)


now = datetime.now()
s = sched.scheduler(time.time, time.sleep)
columns = ['Time', 'Log']
random_logs = ['detected motion at (40, 30)', 'saw a cat', 'saw a bird', 'Mail man detected', 'family detected']
df = pd.DataFrame(columns = columns)





def record_camera(sc,df):     
    current_time = now.strftime("%H:%M:%S")
    log_info = (random.choice(random_logs))
    log.info(log_info)
    df = df.append(pd.Series([current_time,log_info],index= columns),ignore_index = True)
    # do your stuff
    try:
        r = requests.get(url = API_ENDPOINT, timeout=30)
        
    except Timeout as ex:
        print("Exception Raised: ", ex)
    #dictToSend = {'question':'what is the answer?'}

    if (r.content) == b'get_logs':
        data = df.to_json(orient ='index')
        
        try:
            res=requests.post(url = API_ENDPOINT_POST, json=data,timeout=30) 
            print('response from server:',res.text)
        except Timeout as ex:
            print ("Exception Raised: ", ex)
    #print(stream.getvalue())
    s.enter(10, 1, record_camera, (sc,df))

s.enter(10, 1, record_camera, (s,df))
s.run()
