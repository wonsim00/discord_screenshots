class Resource:
    @property
    def image_base_url(self):
        return 'https://cdn.discordapp.com'

    def __init__(self, **kwargs):
        for key in kwargs:
            if kwargs[key]:
                self.__attrs[key] = kwargs[key]
    
    def __getattr__(self, key):
        if key == '_Resource__attrs':
            super(Resource, self).__setattr__(key, {})
            return self.__attrs
        elif key in self.__attrs:
            return self.__attrs[key]
        raise AttributeError
    
    def __setattr__(self, key, value):
        if key not in self.__attrs:
            self.__attrs[key] = value
        else:
            raise AttributeError
    
    def _set_private_attr(self, key, value):
        super(Resource, self).__setattr__(f'_{type(self).__name__}{key}', value)