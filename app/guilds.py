from .app import app
from components import Guild

from flask import abort, render_template
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

    return render_template(
        "guilds.html", 
        guilds="\n".join(map(str, guilds))
    )