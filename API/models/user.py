from core.base import reClass



class UserDetails:
    def __init__(self, _id=None, uuid=None, email=None, password=None, token=None):
        self._id        : str = _id
        self.uuid       : str = uuid
        self.email      : str = email
        self.password   : str = password
        self.token      : str = token


class TokenSchema(reClass.Schema):
    expire   = reClass.fields.String()
    token    = reClass.fields.String()


class UserDetailsSchema(reClass.Schema):
    uuid        = reClass.fields.String()
    email       = reClass.fields.Email()
    password    = reClass.fields.String()
    token       = reClass.fields.String()


class LoadedUsers(UserDetailsSchema, reClass.Schema):
    _id = reClass.fields.Field()

    @reClass.post_load
    def make(self, data, **kwargs):
        return UserDetails(**data)
