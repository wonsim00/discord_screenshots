from .resource import Resource

class Attachment(Resource):
    @property
    def is_image(self):
        return hasattr(self, 'width') and hasattr(self, 'height')
    
    @staticmethod
    def from_dict(kwargs):
        return Attachment(**kwargs)
    
    @staticmethod
    def to_attachment_list(object_list):
        return list(Attachment.from_dict, object_list)