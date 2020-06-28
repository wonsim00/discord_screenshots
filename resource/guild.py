from .resource import Resource
from .channel import Channel

class Guild(Resource):
    def __init__(self, **kwargs):
        super(Guild, self).__init__(**kwargs)
        self._set_private_attr('__channels', [])
        self._set_private_attr('__channel_ids', set())

    @property
    def resource_guild_icon(self):
        return f'{self.image_base_url}/icons/{self.id}/{self.icon}.png'
    
    @property
    def resource_guild_splash(self):
        return f'{self.image_base_url}/splashes/{self.id}/{self.splash}.png'
    
    @property
    def resource_guild_discovery_splash(self):
        return f'{self.image_base_url}/discovery-splashes/{self.id}/{self.discovery_splash}.png'
    
    @property
    def resource_guild_banner(self):
        return f'{self.image_base_url}/banners/{self.id}/{self.banner}.png'
    
    @property
    def url_channels(self):
        return f'/guilds/{self.id}/channels'
    
    @property
    def channels(self):
        for channel in self.__channels:
            yield channel
    
    def add_channel(self, channel):        
        if not isinstance(channel, Channel):
            channel = Channel.from_dict(channel)
        if channel.guild_id != self.id:
            raise RuntimeError
        
        if channel.id in self.__channel_ids:
            raise RuntimeError
        self.__channel_ids.add(channel.id)
        self.__channels.append(channel)
    
    @staticmethod
    def from_dict(kwargs):
        return Guild(**kwargs)
    
    def __repr__(self):
        return f'<Guild {self.id} of name `{self.name}`>'