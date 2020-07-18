from .app import app
from resources import Guild
from utils.flask import my_render_template

from flask import abort
import json as _json

def guilds():
    try:
        res = app._client.api_get('/users/@me/settings')
        guild_ids = res.json()['guild_positions']
        guild_id_order = { guild_id: idx for (idx, guild_id) in enumerate(guild_ids)}
        
        res = app._client.api_get('/users/@me/guilds')
        guilds = sorted(
            map(Guild.from_dict, res.json()),
            key = lambda x: guild_id_order[x.id] )
    except _json.JSONDecodeError:
        raise abort(500)

    return my_render_template("guilds.html", guilds=guilds, getattr=getattr)