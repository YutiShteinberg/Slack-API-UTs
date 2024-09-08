from slack import app

def post_message(channel, text):
    try:
        app.client.chat_postMessage(channel = channel, text = text)
    except Exception as e:
        raise e

def post_personal_message(channel, text, user):
    try:
        app.client.chat_postEphemeral(channel = channel, user = user, text=text)
    except Exception as e:
        raise e

def create_channel(name, is_private):
    try:
        app.client.conversations_create(name = name, is_private = is_private)
    except Exception as e:
        raise e
    
def update_message(channel, ts, user):
    try:
        app.client.chat_update(channel = channel, user = user, ts = ts)
    except Exception as e:
        raise e
    
def delete_message(channel, message_ts):
    try:
        app.client.chat_delete(channel = channel, ts = message_ts)
    except Exception as e:
        raise e

def get_channel_history(channel):
    try:
        history = app.client.conversations_history(channel)
        return history
    except Exception as e:
        raise e
