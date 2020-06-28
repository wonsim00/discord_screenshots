from .resource import Resource
from .user import User
from utils.time import parse_timestamp_local
from utils.decorators import cached

class Message(Resource):
    __CONVERTER = cached({
        'author': User.from_dict,
        'timestamp': parse_timestamp_local,
        'edited_timestamp': parse_timestamp_local,
        'attachments': tuple,
        'embeds': tuple,
        'mentions': tuple,
        'mention_roles': tuple 
    })
    
    def __main__(self, **kwargs):
        for key in self.__CONVERTER:
            if key in kwargs:
                kwargs[key] = self.__CONVERTER[key](kwargs[key])
        super(Message, self).__init__(**kwargs)