import hashlib

from base import database_handler, reClass

from models.user import LoadedUsers, UserDetails, UserDetailsSchema

from .schema import SchemaString

query = reClass.TQuery()
mutation = reClass.TMutation()


class UserConnect:
    def __init__(self) -> None:
        self.__db = None
        self.__autoconnect()

    def __autoconnect(self):
        self.__db = database_handler().connected

    def __get_database(self, arg: str) -> reClass.MongoClient:
        arg = arg.lower()
        switch_case = {"user": self.__db["Project251"]["Users"], "shop": self.__db}
        return switch_case.get(arg, None)

    def user_database_query(self, query, exclude=None):
        user = self.__get_database("user")
        res = None
        if exclude is None:
            res = user.find_one(query)
        else:
            res = user.find_one(query, **exclude)
        return res

    def create_account(self, data):
        user = self.__get_database("user")
        user.insert_one(data)


AU = UserConnect()


@query.field("echo")
def echo(*_, message):
    return message


@mutation.field("SignUp")
def ql_SignUp(*_, account):
    hashed = hashlib.md5(account["password"].encode()).hexdigest()
    current: UserDetails = UserDetails(
        None, reClass.uuid.uuid4(), account["email"], hashed
    )
    current.token.expire = ""
    current.token.token = ""
    if not AU.user_database_query({"email": current.email}):
        entry = UserDetailsSchema().dump(current)
        AU.create_account(entry)
        reClass.pprint(entry)
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
        return query
    else:
        return


GraphQl = reClass.CreateSchema(SchemaString, [query, mutation])
