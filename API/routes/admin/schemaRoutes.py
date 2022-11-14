import hashlib

from core import reClass, DatabaseConnecter

from models.user import LoadedUsers, UserDetails, UserDetailsSchema
from models.admin import LoadedAdmin, AdminDetails, AdminDetailsSchema

from .schema import SchemaString

query = reClass.TQuery()


AU = DatabaseConnecter

@query.field("Users")
def ql_Users(*_):
    query = AU.users_database_query_many({})
    x = []
    for i in query:
        x.append(i)
    return x

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
        entry : UserDetails = LoadedUsers().load(query) 
        # TODO: check admin data
        query_admin = AU.admin_database_query({"token": entry.token})
        if (query_admin is not None):
            admin_entry : AdminDetails = LoadedAdmin().load(query_admin)
            if entry.uuid == admin_entry.uuid:
                return query_admin
        return
    else:
        return


GraphQl = reClass.CreateSchema(SchemaString, [query])
