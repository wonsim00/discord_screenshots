from flask import abort, redirect, render_template, request

from .app import app
from .guilds import guilds as _guilds
from .login import login as _login

@app.route("/")
def root():
    if app._client:
        return redirect("/home")
    else:
        return redirect("/login")

@app.route("/home")
def home():
    return redirect("/guilds")

app.add_url_rule('/guilds', _guilds.__name__, _guilds)
app.add_url_rule('/login', _login.__name__, _login, methods = ['GET', 'POST'])