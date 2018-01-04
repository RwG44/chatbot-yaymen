# -*- coding: utf8 -*-
import os
import json
import requests
import app
import nlp_process as nlp

def main_process(data):
    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message
                    try:
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        #recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message = messaging_event["message"]
                        
                        if message.get("text"):
                            message_text = message["text"]  # the message's text
                            reply_text = nlp.nlp_process(message_text)
                            
                            send_message(sender_id, reply_text)
                        if message.get("attachments"):
                            for attachment in message.get("attachments"):
                                mtype = attachment["type"]
                                url = attachment["payload"]["url"]  # the message's url                            
                                send_attachment(sender_id, mtype, url)
                    except Exception as ex:
                        app.log("Error..: " + str(ex))

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button
                    pass

def send_message(recipient_id, message_text):

    app.log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    res = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if res.status_code != 200:
        app.log(res.status_code)
        app.log(res.text)

def send_attachment(recipient_id, mtype, url):

    app.log("sending attachment to {recipient}: {mtype}".format(recipient=recipient_id, mtype=mtype))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment":{
                "type":mtype, 
                "payload":{
                    "url":url, 
                    "is_reusable": "true"
                    }
            }
        }       
    })
    #data = json.load(open("image.json"))
    res = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if res.status_code != 200:
        app.log(res.status_code)
        app.log(res.text)
        