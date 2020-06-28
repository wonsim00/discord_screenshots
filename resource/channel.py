from .resource import Resource
from .message import Message
from utils.decorators import cached

class Channel(Resource):
    def __init__(self, **kwargs):
        super(Channel, self).__init__(**kwargs)
        self._set_private_attr('__messages', [])
        self._set_private_attr('__message_ids', set())
    
    @property
    def messages(self):
        for message in self.__messages:
            yield message
    
    @property
    def oldest_message_id(self):
        if len(self.__messages):
            return self.__messages[-1].id
        return None
    
    @property
    def url_messages(self):
        return f'/channels/{self.id}/messages'
    
    def add_message(self, message):        
        if not isinstance(message, Message):
            message = Message.from_dict(message)
        if message.channel_id != self.id:
            raise RuntimeError
        
        if message.id in self.__message_ids:
            raise RuntimeError
        self.__message_ids.add(message.id)
        self.__messages.append(message)

    @staticmethod
    def from_dict(kwargs):
        return Channel(**kwargs)
    
    def __repr__(self):
        return f'<Channel {self.id} of name `{self.name}` and type `{types.from_index(self.type)}`>'

class _Types:
    __keys = cached([
        'GUILD_TEXT',
        'DM',
        'GUILD_VOICE',
        'GROUP_DM',
        'GUILD_CATEGORY',
        'GUILD_NEWS',
        'GUILD_STORE'
    ])
    __obj = None

    @staticmethod
    def get_object():
        if _Types.__obj == None:
            _Types.__obj = _Types()
        return _Types.__obj
    
    def __init__(self):
        self.__indices = {}
        for idx, key in enumerate(self.__keys):
            self.__indices[key] = idx
    
    def __getattr__(self, key):
        if key in self.__indices:
            return self.__indices[key]
        raise IndexError
    
    def from_index(self, index):
        return self.__keys[index]

types = _Types.get_object()