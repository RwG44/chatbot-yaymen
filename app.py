# -*- coding: utf8 -*-
import os
import sys
import json
from datetime import datetime
from flask import Flask, request, render_template
import message_process as mp
import test

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world! This is chatbot at {time}".format(time=datetime.now()), 200

@app.route('/test', methods=['POST'])
def testinput():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    input = request.form["input"]
    if input != "":
       reply = test.test_main(input)
       return render_template("test.html", result = reply)
    else:
        return render_template("test.html", result = "No input")


@app.route('/test', methods=['GET'])
def testinput2():
    return render_template("test.html")

@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
    data = request.get_json()    
    log(data)  # you may not want to log every incoming message in production, but it's good for testing
    mp.main_process(data)
    return "ok", 200

def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = msg.format(*args, **kwargs)
        #print u"{}: {}".format(datetime.now(), msg)
        print(msg)
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

if __name__ == '__main__':
    app_location = os.environ.get('APP_LOCATION', "Null")
    log("starting server at " + app_location)
    if app_location == 'heroku':
        app.run(debug=False)
    if app_location == 'openshift':
        # Get the environment information we need to start the server
        ip = os.environ['OPENSHIFT_PYTHON_IP']
        port_num = int(os.environ['OPENSHIFT_PYTHON_PORT'])
        host_name = os.environ['OPENSHIFT_GEAR_DNS']
        log("Running at {ip}, {host_name}, {port_num}".format(ip,host_name,port_num))
        app.run(debug=True, host=ip, port= port_num)
    else:
        app.run(debug=True, host="127.0.0.1", port= 8080)
    log("finished at starting server")
    #heroku local web -f Procfile.windows
    #heroku ps:scale web=1
