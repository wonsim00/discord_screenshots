from .component import Component
from .message import Message

class MessageBlock(Component):
    def __init__(self, username, avatar, timestamp, messages):
        self.username = username
        self.avatar = avatar
        self.timestamp = timestamp

        self.messages = []
        for idx, message in enumerate(messages):
            if idx == 0:
                obj = Message(message, True, username, avatar, timestamp)
            else:
                obj = Message(message)
            self.messages.append(obj)
    
    def html(self):
        return "{}" # TODO
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        try:
            self.__username
            raise RuntimeError
        except AttributeError:
            self.__username = value
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        try:
            self.__timestamp
            raise RuntimeError
        except AttributeError:
            self.__timestamp = value