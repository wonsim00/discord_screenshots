from .resource import Resource
from utils.decorators import cached

class User(Resource):
    __REGISTERED = cached({})

    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            raise AttributeError
        
        user_id = kwargs['id']
        if user_id in self.__REGISTERED:
            raise ValueError
        
        super(User, self).__init__(**kwargs)
        self.__REGISTERED[user_id] = self
    
    @property
    def resource_user_icon(self):
        return f'{self.image_base_url}/avatars/{self.id}/{self.avatar}.png'

    @staticmethod
    def get_by_id(user_id):
        if user_id in User.__REGISTERED:
            return User.__REGISTERED[user_id]
        raise IndexError

    @staticmethod
    def from_dict(kwargs):
        try:
            return User(**kwargs)
        except ValueError:
            return User.get_by_id(kwargs['id'])
    
    def __repr__(self):
        return f'<User {self.id} of username `{self.username}`>'