from core import reClass

class DeviceDetails:
    def __init__(self, _id="", uuid="", name="", listing={}, alias=""):
        self._id        : str = _id
        self.alias      : str = alias
        self.uuid       : str = uuid
        self.name       : str = name
        self.listing    : list = listing

class DeviceDetailsSchema(reClass.Schema):
    uuid        = reClass.fields.String()
    alias       = reClass.fields.String()
    name        = reClass.fields.String()
    listing     = reClass.fields.Dict()

class LoadedDevice(DeviceDetailsSchema, reClass.Schema):
    _id = reClass.fields.Field()

    @reClass.post_load
    def make(self, data, **kwargs):
        return DeviceDetails(**data)
