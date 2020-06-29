class Resource:
    @property
    def image_base_url(self):
        return 'https://cdn.discordapp.com'

    def __init__(self, **kwargs):
        self._set_private_attr('__attrs', {})

        for key in kwargs:
            if kwargs[key] != None:
                self.__attrs[key] = kwargs[key]
    
    def __getattr__(self, key):
        if key in self.__attrs:
            return self.__attrs[key]
        raise AttributeError
    
    def __setattr__(self, key, value):
        if key not in self.__attrs:
            self.__attrs[key] = value
        else:
            raise AttributeError
    
    def _set_private_attr(self, key, value):
        super(Resource, self).__setattr__(f'_{type(self).__name__}{key}', value)