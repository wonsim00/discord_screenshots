from flask import abort, redirect, render_template, request

from api import DiscordApiClient
from .app import app

def login():
    if request.method == 'GET':
        if app._client:
            return redirect("/home")
        else:
            return render_template("login.html")
    else:
        if app._client:
            abort(400)
        else:
            data = request.form
            app._client = DiscordApiClient(data['email'], data['password'])
            return redirect("/home")