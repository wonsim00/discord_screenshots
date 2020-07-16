from .app import app
from resources import Guild
from utils.flask import my_render_template

from flask import abort
import json as _json

def guilds():
    try:
        res = app._client.api_get('/users/@me/settings')
        guild_ids = res.json()['guild_positions']
        guilds = []

        for guild_id in guild_ids:
            res = app._client.api_get(f'/guilds/{guild_id}')
            guilds.append(Guild.from_dict(res.json()))
    except _json.JSONDecodeError:
        raise abort(500)

    return my_render_template("guilds.html", guilds=guilds, getattr=getattr)