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


class Bank:
    def __init__(self, amount, limit):
        self.amount = amount
        self.limit = limit


class Currency:
    def __init__(self, bank, wallet):
        self.bank: Bank = bank
        self.wallet = wallet


class BankSchema(Schema):
    amount = fields.Number()
    limit = fields.Number()

    @post_load
    def make(self, data, **kwargs):
        return Bank(**data)


class CurrencySchema(Schema):
    bank = fields.Nested(BankSchema)
    wallet = fields.Float()

    @post_load
    def make(self, data, **kwargs):
        return Currency(**data)
