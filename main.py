from threading import Thread
from api import MyJsonApi
from app import app
from config import config
import time
import webview

def run_app():
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(port = port)

def copy_file(src, dst):
    with open(src, "rb") as src_file:
        with open(dst, "wb") as dst_file:
            dst_file.write(src_file.read())

def copy_files():
    for elem in config.environ.copy_files:
        copy_file("."+elem.source, "."+elem.destination)

if __name__=='__main__':
    copy_files()

    port = config.app_configurations.port
    debug = config.environ.debug

    if debug:
        run_app()
    else:
        open_window_after = config.app_configurations.open_window_after
        title = config.app_configurations.title
        width = config.app_configurations.width
        height = config.app_configurations.height
        gui = getattr(config.environ, 'gui', None)

        api = MyJsonApi()

        t = Thread(target=run_app)
        t.daemon = True
        t.start()

        time.sleep(open_window_after)
        window = webview.create_window(
            title = title,
            url = f'http://127.0.0.1:{port}/',
            width = width,
            height = height,
            js_api = api
        )

        api.window = window
        api.config = config
        webview.start(gui = gui)