from .app import app
from resources import Message
from utils.flask import my_render_template
from components import *

def channel_messages(channel_id):
    return my_render_template("channel_messages.html", screenshot=f"/channels/{channel_id}/screenshot")

def channel_screenshot(channel_id):
    res = app._client.api_get(f'/channels/{channel_id}/messages')
    messages = list(map(Message.from_dict, res.json()))
    screenshot = Screenshot(messages)
    return my_render_template("channel_screenshot.html", screenshot=str(screenshot))