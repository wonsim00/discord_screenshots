from .app import app
from resources import Channel
from utils.flask import my_render_template

from operator import itemgetter as _itemgetter

def guild_channels(guild_id):
    res = app._client.api_get(f'/guilds/{guild_id}/channels')
    channels = sorted(map(Channel.from_dict, res.json()), key = _itemgetter('position'))
    