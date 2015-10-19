from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from src.utils.memReport import memReport
import subprocess
from src.utils.media_downloader import ImageSender, VideoSender, YoutubeSender, UrlPrintSender, GoogleTtsSender
import os

class MediaViews():
    def __init__(self, interface_layer):

        self.image_sender = ImageSender(interface_layer)
        self.google_tts_sender = GoogleTtsSender(interface_layer)
        self.routes = [
            ("^sendimage\s(?P<image>[^$]+)", self.send_image),
            ("^say\s(?P<say>[^$]+)", self.send_tts)
        ]

    def send_image(self, message, match):
        self.image_sender.send_by_path(jid=message.getFrom(), path= os.getcwd() + '/images/' + match.group('image'))

    def send_tts(self, message, match):
        self.google_tts_sender.send(jid=message.getFrom(), text=match.group("say"), lang='en')

def hello(message, match):
    output = ['List of commands: ', 'Hello', 'startServer', 'memoryUsage', 'prepareDemo']
    print message.getFrom()
    return TextMessageProtocolEntity('\n'.join(output), to=message.getFrom())

def start_server(message, match):
    output = subprocess.check_output(['ls', '-1'])
    return TextMessageProtocolEntity(output, to=message.getFrom())

def exec_command(message, match):
    commands = match.group('exec_command').split(' ')
    command = commands[0]
    parameters = commands[1:]
    output = subprocess.check_output([command, ' '.join(parameters)])
    return TextMessageProtocolEntity(output, to=message.getFrom())

def memory_usage(message, match):
    output = memReport()
    return TextMessageProtocolEntity('\n'.join(output), to=message.getFrom())

def preparing_demo(message, match):
    return TextMessageProtocolEntity('Something awesome is cooking', to=message.getFrom())


routes = [("^Hello", hello),
          ("^startServer", start_server),
          ("^memoryUsage", memory_usage),
          ("^prepareDemo", preparing_demo),
          ("^/exec\s(?P<exec_command>[^$]+)", exec_command)]
