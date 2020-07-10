from .component import Component


class Avatar(Component):
    def __init__(self, path):
        self.path = path
    
    def html(self):
        return '<img src="{path}" class="avatar" />'.format(path=self.path)


class Username(Component):
    def __init__(self, username):
        self.username = username
    
    def html(self):
        return '<span class="username">{username}</span>'.format(username=self.username)


class Timestamp(Component):
    def __init__(self, timestamp):
        self.timestamp = timestamp
    
    def html(self):
        return '<span class="timestamp">{timestamp}</span>'.format(timestamp=self.timestamp)


class Header(Component):
    def __init__(self, username, avatar, timestamp):
        self.username = username
        self.avatar = avatar
        self.timestamp = timestamp
    
    def html(self):
        return '<div class="content">{avatar}<h2 class="header">{username}{timestamp}</h2></div>'.format(
            avatar = self.avatar, username = self.username, timestamp = self.timestamp )


class Message(Component):
    def __init__(self, content, header = False, username = None, avatar = None, timestamp = None):
        self.content = content
        if header:
            self.header = Header(username, avatar, timestamp)
        else:
            self.header = ""
    
    def html(self):
        return f'<div class="message">{self.header}<div class="messageContent">{self.content}</div></div>'