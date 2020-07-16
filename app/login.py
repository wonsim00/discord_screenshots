from flask import abort, redirect, render_template, request
import json as _json

from api import DiscordApiClient
from .app import app

def login():
    if request.method == 'GET':
        if app._client:
            return redirect("/home")
        else:
            login_failed = json.loads(request.args.get('login_failed', 'false'))
            return render_template("login.html")
    else:
        if app._client:
            abort(400)
        else:
            data = request.form
            try:
                app._client = DiscordApiClient(data['email'], data['password'])
                return redirect("/home")
            except RuntimeError:
                return redirect("/login?login_failed=true")