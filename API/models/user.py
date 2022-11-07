from base import reClass


class Token:
    def __init__(self, expire=None, token=None):
        self.expire: str = expire
        self.token: str = token


class UserDetails:
    def __init__(self, _id=None, uuid=None, email=None, password=None, token=Token()):
        self._id: str = _id
        self.uuid: str = uuid
        self.email: str = email
        self.password: str = password
        self.token: Token = token


class TokenSchema(reClass.Schema):
    expire = reClass.fields.String()
    token = reClass.fields.String()


class UserDetailsSchema(reClass.Schema):
    uuid = reClass.fields.String()
    email = reClass.fields.Email()
    password = reClass.fields.String()
    token = reClass.fields.Nested(TokenSchema)


class LoadedUsers(UserDetailsSchema, reClass.Schema):
    _id = reClass.fields.Field()

    @reClass.post_load
    def make(self, data, **kwargs):
        return UserDetails(**data)
