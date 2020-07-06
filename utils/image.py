import PIL.Image as _Image
import io as _io

def load_image_from_bytes(bytes):
    return _Image.open(_io.BytesIO(bytes))