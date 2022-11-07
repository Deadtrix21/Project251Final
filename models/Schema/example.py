from pprint import pprint

data = {
    "Inventory": [],
    "Boosts": {},
    "Discord_Id": 123456,
    "Exp": {"exp": 0.0, "lvl": 0},
    "Clan_Id": 0,
    "Currency": {"bank": {"amount": 0.0, "limit": 50000.0}, "wallet": 5000.0},
    "Staff": {"enable": False, "category": "None"},
    "Account": {
        "email": "example@outlook.com",
        "created_at": "2022-04-02T21:55:27.798175+02:00",
        "since_created": 0,
        "password": "exmaple",
    },
}
pprint(data, indent=5)
{
    "Account": {
        "created_at": "2022-04-02T21:55:27.798175+02:00",
        "email": "example@outlook.com",
        "password": "exmaple",
        "since_created": 0,
    },
    "Boosts": {},
    "Clan_Id": 0,
    "Currency": {"bank": {"amount": 0.0, "limit": 50000.0}, "wallet": 5000.0},
    "Discord_Id": 123456,
    "Exp": {"exp": 0.0, "lvl": 0},
    "Inventory": [],
    "Staff": {"category": "None", "enable": False},
}
