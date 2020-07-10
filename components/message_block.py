from .component import Component
from .message import Message

class MessageBlock(Component):
    def __init__(self, username, avatar, timestamp, messages):
        self.username = username
        self.avatar = avatar
        self.timestamp = timestamp

        self.messages = []
        for idx, message in enumerate(messages):
            content = message.content
            if idx == 0:
                obj = Message(content, True, username, avatar, timestamp)
            else:
                obj = Message(content)
            self.messages.append(obj)
    
    def html(self):
        return "".join(map(str, self.messages))
    
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
    def avatar(self):
        return self.__avatar
    
    @avatar.setter
    def avatar(self, value):
        try:
            self.__avatar
            raise RuntimeError
        except AttributeError:
            self.__avatar = value
    
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