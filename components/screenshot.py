from .component import Component
from .message_block import MessageBlock
from .message import Avatar, Username

from utils.time import trim_minute
from utils.decorators import cached

class Screenshot(Component):
    class User:
        def __init__(self, user_id, username, avatar):
            self.__user_id = user_id
            self.__username = username
            self.__avatar = avatar
        
        @property
        def user_id(self):
            return self.__user_id
        
        @property
        def username(self):
            return self.__username
        
        @property
        def avatar(self):
            return self.__avatar

    def __init__(self, messages):
        if len(messages) == 0:
            raise ValueError
        self._generate_message_blocks(messages)

    def _generate_message_blocks(self, messages):
        self.__users = {}
        self.__message_blocks = {}

        current_user_id = None
        current_timestamp = None
        tmp_list = []

        for message in messages:
            if current_user_id and (
                message.author.id != current_user_id or
                (trim_minute(message.timestamp)-trim_minute(current_timestmp)).total_seconds() >= 4200
            ):
                user_id = tmp_list[0].author.id
                if user_id in self.__users:
                    user = self.__users[user_id]
                else:
                    username = tmp_list[0].author.username
                    avatar = tmp_list[0].author.resource_user_avatar
                    timestamp = tmp_list[0].timestamp
                    
                    user = User(user_id, Username(username), Avatar(avatar), Timestamp(timestamp))
                    self.__users[user_id] = user
                
                message_block = MessageBlock(user.username, user.avatar, user.timestamp, tmp_list)
                self.__message_blocks.append(message_block)
                tmp_list.clear()