import requests as _requests

class DiscordApiClient(_requests.Session):
    __token = None

    @property
    def __authorization(self):
        return self.__token
    
    @__authorization.setter
    def __authorization(self, val):
        if not self.__token:
            self.__token = val

    @property
    def _base_url(self):
        return 'https://discord.com/api/v6'

    def __init__(self, email, password):
        super(DiscordApiClient, self).__init__()
        res = self.api_post('/auth/login', json = {
            'email': email, 'password': password
        })

        if res.status_code != 200:
            raise RuntimeError

        self.__authorization = res.json()['token']
    
    def api_request(self, method, url, **kwargs):
        if self.__authorization:
            self.headers.update({'authorization': self.__authorization})

        return super(DiscordApiClient, self).request(
            method = method, url = f'{self._base_url}{url}', **kwargs
        )
    
    def api_get(self, url, **kwargs):
        return self.api_request('GET', url, **kwargs)
    
    def api_post(self, url, **kwargs):
        return self.api_request('POST', url, **kwargs)
    
    def api_delete(self, url, **kwargs):
        return self.api_request('DELETE', url, **kwargs)
    
    def api_patch(self, url, **kwargs):
        return self.api_request('PATCH', url, **kwargs)