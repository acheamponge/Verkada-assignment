# *Verkada* Take Home Assignment


## How to run the application

- Install all dependencies by running pip install -r requirements.txt in the folder
- Run python api_server.py first to start the API server (API server runs on 127.0.0.1:8080/)
- Run python web_client.py to start the web client (web client runs on 127.0.0.1:5000/)
- Run python virtual_camera.py to start the virtual camera
- send a GET request to 127.0.0.1:5000/logs (web_client side) either by entering into a web browser, using POSTMAN or sending POST request from command line
*PS - the /logs takes a little time to populate at first so you need to send it at least twice in the beggining*