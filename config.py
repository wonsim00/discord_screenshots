import json as _json

class _Config:
    def __init__(self, config_json):
        if isinstance(config_json, dict):
            super(_Config, self).__setattr__("_Config__value", {})
            for key in config_json:
                self.__value[key] = _Config(config_json[key])
        elif isinstance(config_json, list) and len(config_json) and isinstance(config_json[0], dict):
            super(_Config, self).__setattr__("_Config__value", [])
            for elem in config_json:
                self.__value.append(_Config(elem))
        else:
            super(_Config, self).__setattr__("_Config__value", config_json)
    
    def __getattr__(self, key):
        if isinstance(self.__value, dict) and key in self.__value:
            return self.__value[key].__get__(None, None)
        return super(_Config, self).__getattribute__(key)
    
    def __setattr__(self, key, value):
        if isinstance(self.__value, dict):
            if key not in self.__config:
                self.__config[key] = value
            else:
                raise AttributeError
        else:
            return super(_Config, self).__setattr__(key, value)
    
    def __get__(self, instance, owner = None):
        if isinstance(self.__value, dict):
            return self
        else:
            return self.__value
    
    def __set__(self, instance, value):
        raise AttributeError

with open("config.json", "r", encoding = "utf8") as f:
    config = _Config(_json.loads(f.read()))