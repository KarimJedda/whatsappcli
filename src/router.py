"""
    The Route Layer.

    Here the message is routed to its proper view.
    The routes are defined with regular expressions and callback functions (just like any web framework).
"""

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
import threading
import re

from routes import MediaViews
from routes import routes

class RouteLayer(YowInterfaceLayer):
    def __init__(self):
        super(RouteLayer, self).__init__()
        routes.extend(MediaViews(self).routes)  # Adds the auto download media routes

        self.views = [(re.compile(pattern), callback) for pattern, callback in routes]

    @ProtocolEntityCallback("message")
    def on_message(self, message):
        self.toLower(message.ack(True))
        if message.getType() == 'text':
            threading.Thread(target=self.route, args=(message,)).start()

    def route(self, message):
        text = message.getBody()
        for route, callback in self.views:
            match = route.match(text)
            if match:
                # message = incoming
                # data = outgoing
                data = callback(message, match)
                if data:
                    self.toLower(data)  # if callback returns a message entity, send it.
                break

    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        self.toLower(entity.ack())
