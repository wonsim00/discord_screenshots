from .app import app
from resources import User

from flask import send_file
import io as _io

def user_avatar(user_id):
    user = User.get_by_id(user_id)
    if not hasattr(user, 'avatar_raw'):
        res = app._client.get(user.resource_user_avatar)
        user.avatar_raw = res.content
    
    return send_file(
        _io.BytesIO(user.avatar_raw),
        mimetype = "image/png"
    )