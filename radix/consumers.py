

from channels import Group

def ws_connect(message):
    print("ws_connect consumer: Someone is connected.")
    path = message['path']                                                     # i.e. /sensor/
    
    if path == b'/radix/temperature':
        print("ws_connect consumer:Adding new user to sensor group")
        Group("sensor").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to radix group...",
        })
    elif path == b'/radix/humidity':
        print("ws_connect consumer:Adding new user to sensor group")
        Group("sensor_humidity").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to radix group...",
        })
        
    else:
		print("Strange connector!!")

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
	print("sensor.js send:"+ message['text'])
	print("ws_message consumer: Received " + message['text'])


def ws_disconnect(message):
    print("ws_disconnect consumer: Someone left us...")
    Group("sensor").discard(message.reply_channel)
    Group("sensor_humidity").discard(message.reply_channel)

