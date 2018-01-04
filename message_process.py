import os
import sys
import json
from datetime import datetime
import requests

def main_process(data)
    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message
                    try:
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message = messaging_event["message"]
                        reply_text = "Nothing"

                        if message.get("text"):
                            message_text = message["text"]  # the message's text
                            reply_text = nlp_process(message_text)
                            send_message(sender_id, reply_text)
                        if message.get("attachments"):
                            type = message["attachments"]["type"]
                            url = message["attachments"]["payload"]["url"]  # the message's url
                            reply_text = message_text
                            send_attachment(sender_id, type, url)
                        
                    except Exception as expt :
                        log("Error..: ")

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

def nlp_process(text):
    return ("Hello there!: " + text);

def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

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
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

def send_attachment(recipient_id, type, url):

    log("sending attachment to {recipient}: {type}".format(recipient=recipient_id, type=type))

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
                "type":type, 
                "payload":{
                    "url":url, 
                    "is_reusable":true
                    }
            }
        }       
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)