from .component import Component
from resources import Guild as _Guild


_DEFAULT_GUILD_ICON_PATH="/static/default_guild_icon.png"

class Guild(Component):
    def __init__(self, guild):
        self.id = guild.id
        self.name = guild.name
        try:
            self.icon = guild.resource_guild_icon
        except AttributeError:
            self.icon = _DEFAULT_GUILD_ICON_PATH
    
    @property
    def id(self):
        return self.__name
    
    @id.setter
    def id(self, value):
        try:
            self.__id
            raise AttributeError
        except AttributeError:
            self.__id = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        try:
            self.__name
            raise AttributeError
        except AttributeError:
            self.__name = value
    
    @property
    def icon(self):
        return self.__icon
    
    @icon.setter
    def icon(self, value):
        try:
            self.__icon
            raise AttributeError
        except AttributeError:
            self.__icon = value
    
    def html(self):
        return f'<div class="guild"><img class="guild-icon" src="{self.icon}"><a class="guild-link" href="/guilds/{self.id}">{self.name}</a></div>'

    @staticmethod
    def from_dict(kwargs):
        return Guild(_Guild.from_dict(kwargs))