from .component import Component

class MessageBlock(Component):
    def __init__(self, *messages):
        attrs = MessageBlock._validate(*messages)
        self.username = attrs['username']
        self.timestamp = attrs['timestamp']
    
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

    @staticmethod
    def _validate(*messages):
        if len(messages) == 0:
            raise ValueError
        username = messages[0].author.username
        timestamp = messages[0].timestamp

        for message in messages:
            if username != messages[0].author.username:
                raise ValueError
        
        return { 'username': username, 'timestamp': timestamp }