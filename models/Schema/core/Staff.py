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


class Staff:
    def __init__(self, enable=False, category=0):
        self.enable = enable
        self.category = category


class StaffSchema(Schema):
    enable = fields.Boolean()
    category = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return Staff(**data)
