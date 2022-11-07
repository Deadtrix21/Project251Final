import arrow
from marshmallow import (
    EXCLUDE,
    INCLUDE,
    Schema,
    ValidationError,
    fields,
    post_dump,
    post_load,
    pprint,
    pre_dump,
    pre_load,
    validate,
    validates,
)


class Exp:
    def __init__(self, lvl, exp):
        self.lvl = lvl
        self.exp = exp


class ExpSchema(Schema):
    lvl = fields.Integer()
    exp = fields.Number()

    @post_load
    def make(self, data, **kwargs):
        return Exp(**data)
