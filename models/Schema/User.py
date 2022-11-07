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

from .core import *

IAccount = Account
IInventory = Inventory
IExp = Exp
ICurrency = Currency
IStaff = Staff


class Final:
    def __init__(self, _id, Discord_Id, Clan_Id, Exp, Account, Currency, Staff, Boosts):
        self._id = _id
        self.Discord_Id = Discord_Id
        self.Clan_Id = Clan_Id
        self.Exp: IExp.Exp = Exp
        self.Account: IAccount.Account = Account
        self.Currency: ICurrency.Currency = Currency
        self.Staff: IStaff.Staff = Staff
        self.Boosts = Boosts


class UserSchema(Schema):
    # Entry
    _id = fields.Field()
    Clan_Id = fields.Integer()
    Discord_Id = fields.Integer()
    # Nested
    Account = fields.Nested(Account.AccountSchema)
    Currency = fields.Nested(Currency.CurrencySchema)
    Exp = fields.Nested(Exp.ExpSchema)
    Staff = fields.Nested(Staff.StaffSchema)
    Boosts = fields.Constant(constant={})

    @post_load
    def make(self, data, **kwargs):
        return Final(**data)
