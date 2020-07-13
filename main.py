from threading import Thread
from app import app
import time
import webview

def run_app():
    app.run()

t = Thread(target=run_app)
t.daemon = True
t.start()

time.sleep(1)
window = webview.create_window(
    title = 'Discord Screenshots',
    url = 'http://127.0.0.1:5000/',
    width = 600,
    height = 800
)
webview.start()