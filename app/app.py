from flask import Flask

class MyApp(Flask):
    _client = None
    _guilds = {}
    _current_guild = None
app = MyApp(__name__)