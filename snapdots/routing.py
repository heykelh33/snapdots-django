# from channels.routing import route
# channel_routing = [
#     route("http.request", "sensors.consumers.http_consumer"),
# ]

from channels.routing import route
from sensors.consumers import ws_connect, ws_message, ws_disconnect


channel_routing = [
    route('websocket.connect', ws_connect, path=r"^/sensor/$"),
    route('websocket.receive', ws_message),
    route('websocket.disconnect', ws_disconnect),
]
