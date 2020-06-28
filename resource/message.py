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
    
    def __init__(self, **kwargs):
        for key in self.__CONVERTER:
            if key in kwargs:
                kwargs[key] = self.__CONVERTER[key](kwargs[key])
        super(Message, self).__init__(**kwargs)
    
    @staticmethod
    def from_dict(kwargs):
        return Message(**kwargs)
    
    def __repr__(self):
        return '<Message {message_id} of content `{content}` created at `{timestamp}` by `{author_name}`>'.format(
            message_id = self.id,
            content = self.content,
            timestamp = self.timestamp,
            author_name = self.author.username
        )