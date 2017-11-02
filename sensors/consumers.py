import json
from channels import Group

def ws_connect(message):
    print("ws_connect consumer: Someone is connected.")
    #path = message['path']                                                     # the path was fixed in routing.py i.e. /sensor/
    #if path == b'/sensor/':
    print("ws_connect consumer: Adding new user to sensor group")
    Group("sensor").add(message.reply_channel)                                   # Adds user to group sensor for broadcast
    message.reply_channel.send({"accept": True})  # Accept the connection request

       
    # else:
    #     message.reply_channel.send({"close": True})  # No Accept the connection request
    #     print("Strange connector!!")

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
	print("sensor.js send:"+ message['text'])
	print("ws_message consumer: Received " + message['text'])


def ws_disconnect(message):
    print("ws_disconnect consumer: Someone left us...")
    Group("sensor").discard(message.reply_channel)
