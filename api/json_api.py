from base64 import b64decode as _b64decode
from config import config
import webview

class MyJsonApi:
    def download_screenshot(self, data_uri):
        result = self.window.create_file_dialog(
            dialog_type=webview.SAVE_DIALOG,
            save_filename=config.app_configurations.default_download_filename
        )
        header, encoded = data_uri.split(",", 1)
        data = _b64decode(encoded)
        with open(result[0], "wb") as f:
            f.write(data)
        return None