from src.sender.stack import YowsupSendStack
import src.config


admin_number = 'xxxxxxxx@s.whatsapp.net'

def send_simple_message(message):
    gs = YowsupSendStack(src.config.auth, [(admin_number, message)])
    gs.start()

send_simple_message('Hello there, server is messed up.')