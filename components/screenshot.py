from .component import Component
from .message_block import MessageBlock
from .message import Avatar, Username, Timestamp

from utils.time import trim_minute
from utils.decorators import cached

class Screenshot(Component):
    class User:
        def __init__(self, user_id, username, avatar):
            self.__user_id = user_id
            self.__username = username
            self.__avatar = avatar

            self.__original_username = username.username
            self.__original_avatar = avatar.avatar
        
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
        self.__message_blocks = []

        current_user_id = None
        current_timestamp = None
        tmp_list = []

        for message in reversed(messages):
            if current_user_id and (
                message.author.id != current_user_id or
                (trim_minute(message.timestamp)-trim_minute(current_timestamp)).total_seconds() >= 420
            ):
                message_block = self._create_new_message_block(*tmp_list)
                self.__message_blocks.append(message_block)
                tmp_list.clear()
            
            current_user_id = message.author.id
            current_timestamp = message.timestamp
            tmp_list.append(message)
        
        if len(tmp_list):
            message_block = self._create_new_message_block(*tmp_list)
            self.__message_blocks.append(message_block)
    
    def _create_new_message_block(self, *messages):
        user_id = messages[0].author.id
        if user_id in self.__users:
            user = self.__users[user_id]
        else:
            username = messages[0].author.username
            avatar = messages[0].author.resource_user_avatar
            
            user = Screenshot.User(user_id, Username(username), Avatar(avatar))
            self.__users[user_id] = user
        
        timestamp = messages[0].timestamp
        message_block = MessageBlock(user.username, user.avatar, Timestamp(timestamp), messages)
        return message_block
    
    def html(self):
        body_inner = "".join(map(str, self.__message_blocks))
        return f'<!DOCTYPE html><head><link rel="stylesheet" type="text/css" href="style.css"></head><body>{body_inner}</body></html>'