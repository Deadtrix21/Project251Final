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


class Account:
    def __init__(self, password, email, created_at):
        self.password = password
        self.email = email
        self.created_at = arrow.get(created_at)


class AccountSchema(Schema):
    password = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    since_created = fields.Method("get_days_since_created")

    class Meta:
        unknown = EXCLUDE

    def get_days_since_created(self, obj):
        number_of_days = (arrow.now() - obj.created_at).days
        years = number_of_days // 365
        months = (number_of_days - years * 365) // 30
        days = number_of_days - years * 365 - months * 30
        return {"years": years, "months": months, "days": days}

    @post_load
    def make(self, data, **kwargs):
        return Account(**data)
