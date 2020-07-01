import PIL as _PIL
import io as _io

def load_image_from_bytes(bytes):
    return _PIL.Image.open(_io.BytesIO(bytes))