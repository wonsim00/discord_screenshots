from flask import Flask

class MyApp(Flask):
    _client = None
app = MyApp(__name__)