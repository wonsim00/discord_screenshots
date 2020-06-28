from .resource import Resource
from .message import Message

class Channel(Resource):
    def __init__(self, **kwargs):
        super(Channel, self).__init__(**kwargs)
        self._set_private_attr('__messages', [])
        self._set_private_attr('__message_ids', set())
    
    @property
    def messages(self):
        for message in self.__messages:
            yield message
    
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