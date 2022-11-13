import hashlib

from core import reClass, DatabaseConnecter

from models.user import LoadedUsers, UserDetails, UserDetailsSchema

from .schema import SchemaString

query = reClass.TQuery()
mutation = reClass.TMutation()




AU = DatabaseConnecter


@query.field("echo")
def echo(*_, message):
    return message


@mutation.field("SignUp")
def ql_SignUp(*_, account):
    hashed = hashlib.md5(account["password"].encode()).hexdigest()
    current: UserDetails = UserDetails(
        None, f"{reClass.uuid.uuid4()}", account["email"], hashed, reClass.secrets.token_hex()
    )
    if not AU.user_database_query({"email": current.email}):
        double_check = False
        while double_check is not True:
            if AU.user_database_query({"uuid": f"{current.uuid}"}) is None:
                double_check = True
            current.uuid = f"{reClass.uuid.uuid4()}"
        entry = UserDetailsSchema().dump(current)
        AU.create_account(entry)
        entry = LoadedUsers().load(entry)
        entry.password = account["password"]
        entry = LoadedUsers().dump(entry)
        return entry
    else:
        return


@query.field("Login")
def ql_Login(*_, account):
    current = UserDetails(
        _id=None, uuid=None, email=account["email"], password=account["password"]
    )
    hashed = hashlib.md5(account["password"].encode()).hexdigest()
    query = AU.user_database_query({"email": current.email})
    if LoadedUsers().load(query).password != hashed:
        return
    if query is not None:
        entry = LoadedUsers().load(query)
        entry.password = account["password"]
        entry = LoadedUsers().dump(entry)
        return entry
    else:
        return


GraphQl = reClass.CreateSchema(SchemaString, [query, mutation])
