from .app import app
from resources import Channel
from resources.channel import types
from utils.flask import my_render_template

from operator import attrgetter as _attrgetter

def guild_channels(guild_id):
    app._current_guild = app._guilds[guild_id]
    res = app._client.api_get(app._current_guild.url_channels)
    
    channels = [Channel(id="", name="", type=types.GUILD_CATEGORY)]
    channels.extend(sorted(
        map(Channel.from_dict, res.json()),
        key = lambda x: (x.type != types.GUILD_CATEGORY, x.position)
    ))
    
    categories = []
    children = {}
    for channel in channels:
        if channel.type == types.GUILD_CATEGORY:
            categories.append(channel)
            children[channel.id] = []
        elif channel.type == types.GUILD_TEXT:
            parent_id = getattr(channel, 'parent_id', "")
            children[parent_id].append(channel)
    
    for category in categories:
        category.children = children[category.id]
    return my_render_template("guild_channels.html",
        categories=filter(_attrgetter('children'), categories), types=types)