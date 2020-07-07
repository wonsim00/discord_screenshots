from .component import Component


class Avatar(Component):
    def __init__(self, path):
        self.path = path
    
    def html(self):
        return '<img src="{path}" aria-hidden="true" class="avatar" />'.format(path=self.path)


class Username(Component):
    def __init__(self, username):
        self.username = username
    
    def html(self):
        return '<span class="username">{username}</span>'.format(username=self.username)


class Timestamp(Component):
    def __init__(self, timestamp):
        self.timestamp = timestamp
    
    def html(self):
        return '<span class="timestamp">{timestamp}</span>'


class Header(Component):
    def __init__(self, user, timestamp):
        self.avatar = Avatar(None) # TODO
        self.username = Username(user.username)
        self.timestamp = Timestamp(timestamp)
    
    def html(self):
        return '<div>{avatar}<h2 class="header">{username}{timestamp}</h2></div>'.format(
            avatar = self.avatar, username = self.username, timestamp = self.timestamp )


class Message(Component):
    def __init__(self, content, header = False, username = None, timestamp = None):
        self.content = content
    
    def html(self):
        # TODO
        return ""