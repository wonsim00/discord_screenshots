from threading import Thread
from app import app
from config import config
import time
import webview

port = config.app_configurations.port
open_window_after = config.app_configurations.open_window_after
title = config.app_configurations.title
width = config.app_configurations.width
height = config.app_configurations.height

def run_app():
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(port = port)

t = Thread(target=run_app)
t.daemon = True
t.start()

time.sleep(open_window_after)
window = webview.create_window(
    title = title,
    url = f'http://127.0.0.1:{port}/',
    width = width,
    height = height
)
webview.start()