# -*- coding: utf8 -*-
import os
import sys
import json
from datetime import datetime
import message_process as mp

try:
    import gevent.monkey
    gevent.monkey.patch_all()
except:
    pass

import bottle
from bottle import default_app, request, route, response, get


@bottle.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@bottle.route('/', methods=['POST'])
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

bottle.run(server='gevent', port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    bottle.debug(True)
