from core.base import reClass

class AdminDetails:
    def __init__(self, _id=None, uuid=None, token=None):
        self._id        : str = _id
        self.uuid       : str = uuid
        self.token      : str = token

class AdminDetailsSchema(reClass.Schema):
    uuid        = reClass.fields.String()
    token       = reClass.fields.String()

class LoadedAdmin(AdminDetailsSchema, reClass.Schema):
    _id = reClass.fields.Field()

    @reClass.post_load
    def make(self, data, **kwargs):
        return AdminDetails(**data)
