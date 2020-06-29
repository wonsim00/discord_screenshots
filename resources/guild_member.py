from .resource import Resource
from .user import User
from utils.time import parse_timestamp_local
from utils.decorators import cached

class GuildMember(Resource):
    __CONVERTER = cached({
        'user': User.from_dict,
        'joined_at': parse_timestamp_local,
        'premium_since': parse_timestamp_local
    })

    def __init__(self, **kwargs):
        for key in self.__CONVERTER:
            if key in kwargs:
                kwargs[key] = self.__CONVERTER[key](kwargs[key])
        
        super(GuildMember, self).__init__(**kwargs)
        self.user.guild_member = self