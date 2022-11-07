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


class InventoryItem:
    def __init__(self):
        pass


class InventoryItemSchema(Schema):
    name = fields.String()

    # @post_load
    def make(self, data, **kwargs):
        return InventoryItem(**data)
