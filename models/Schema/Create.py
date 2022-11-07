import arrow
from marshmallow import (
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
        self.created_at = (
            arrow.get(created_at) if created_at != None else arrow.now().isoformat()
        )


class AccountSchema(Schema):
    password = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    since_created = fields.Method("get_days_since_created")

    def get_days_since_created(self, obj):
        return (arrow.now() - obj.created_at).days


class Exp:
    def __init__(self):
        self.lvl = 0
        self.exp = 0


class ExpSchema(Schema):
    lvl = fields.Integer()
    exp = fields.Number()


class Bank:
    def __init__(self):
        self.amount = 0
        self.limit = 50000

    def __repr__(self):
        return str({"amount": self.amount, "limit": self.limit})


class BankSchema(Schema):
    amount = fields.Number()
    limit = fields.Number()


class Currency:
    def __init__(self):
        self.bank = Bank()
        self.wallet = 5000


class CurrencySchema(Schema):
    bank = fields.Nested(BankSchema)
    wallet = fields.Float()


class Staff:
    def __init__(self, enable=False, category=0):
        self.enable = enable
        self.category = category

    def __repr__(self):
        return str({"enable": self.enable, "category": self.category})


class StaffSchema(Schema):
    enable = fields.Boolean()
    category = fields.Integer()


class InventoryItem:
    def __init__(self):
        pass


class InventoryItemSchema(Schema):
    name = fields.String()


class Final:
    def __init__(self, discord):
        self.Clan_Id = 0
        self.Discord_Id = discord
        self.Exp = Exp()
        self.Account = Account(
            created_at=arrow.now().isoformat(),
            password="exmaple",
            email="example@outlook.com",
        )
        self.Currency = Currency()
        self.Staff = Staff()


class UserSchema(Schema):
    # Entry
    Clan_Id = fields.Integer()
    Discord_Id = fields.Integer()
    # Nested
    Account = fields.Nested(AccountSchema)
    Currency = fields.Nested(CurrencySchema)
    Exp = fields.Nested(ExpSchema)
    Staff = fields.Nested(StaffSchema)
    Boosts = fields.Constant(constant={})
