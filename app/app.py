from flask import Flask, abort, redirect, render_template, request
from api import DiscordApiClient
from components import Guild

app = Flask(__name__)
_client = None


@app.route("/")
def _root():
    global _client
    if _client:
        return redirect("/home")
    else:
        return redirect("/login")

@app.route("/home")
def _home():
    guild_ids = _client.api_get('/users/@me/settings').json()['guild_positions']
    guilds = [
        Guild.from_dict(_client.api_get(f'/guilds/{guild_id}').json())
        for guild_id in guild_ids   ]
    return render_template(
        "guilds.html", 
        guilds="\n".join(map(str, guilds))  )

@app.route("/login", methods = ['GET', 'POST'])
def _login():
    global _client
    if request.method == 'GET':
        if _client:
            return redirect("/home")
        else:
            return render_template("login.html")
    else:
        if _client:
            abort(400)
        else:
            data = request.form
            _client = DiscordApiClient(data['email'], data['password'])
            return redirect("/home")