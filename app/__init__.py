from flask import abort, redirect, render_template, request

from .app import app
from .channels import guild_channels as _guild_channels
from .guilds import guilds as _guilds
from .login import login as _login
from .messages import channel_messages as _channel_messages
from .messages import channel_screenshot as _channel_screenshot

@app.route("/")
def root():
    if app._client:
        return redirect("/home")
    else:
        return redirect("/login")

@app.route("/home")
def home():
    return redirect("/guilds")

app.add_url_rule('/channels/<channel_id>', _channel_messages.__name__, _channel_messages)
app.add_url_rule('/channels/<channel_id>/screenshot', _channel_screenshot.__name__, _channel_screenshot)
app.add_url_rule('/guilds/<guild_id>', _guild_channels.__name__, _guild_channels)
app.add_url_rule('/guilds', _guilds.__name__, _guilds)
app.add_url_rule('/login', _login.__name__, _login, methods = ['GET', 'POST'])