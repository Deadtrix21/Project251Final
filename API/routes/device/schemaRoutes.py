import hashlib

from core import reClass, DatabaseConnecter, DatabaseConnect

from models.user import LoadedUsers, UserDetails, UserDetailsSchema
from models.admin import LoadedAdmin, AdminDetails, AdminDetailsSchema
from models.device import LoadedDevice, DeviceDetails, DeviceDetailsSchema


from .schema import SchemaString

query = reClass.TQuery()
mutation = reClass.TMutation()




AU: DatabaseConnect = DatabaseConnecter


@query.field("echo")
def echo(*_, message):
    return {"msg":message}


@query.field("deviceGet")
def ql_deviceGet(*_, uuid):
    query = AU.device_database_query_many({"uuid":uuid})
    return query

@mutation.field("sectionAlias")
def ql_sectionAlias(*_, name, uuid, alias):
    try:
        AU.device_database_update({"name": name}, {"alias" : alias})
        print(AU.device_database_query({"name": name}))
        return 1
    except Exception:
        print(3)
        return 0


@mutation.field("deviceUpdate")
def ql_deviceUpdate(*_, name, num, state):
    query = AU.device_database_query({"name":name})
    structure = {
        "level" : state["level"],
        "id": num,
        "current" : state["current"]
    }
    print(query)
    try:
        if query != None:
            if "listing" not in query:
                raise EOFError
            entry = LoadedDevice().load(query)
            x, found= 0, False
            for i in entry.listing:
                if i["id"] == num:
                    found = True
                    query["listing"][x] = structure
                else:
                    pass
                x += 1
            if found == False:
                query["listing"].append(structure)
            AU.device_database_del({"name":name})
            AU.create_device(query)
            return 2       
    except EOFError:
        uuid = ""
        if "uuid" in query:
            uuid = query["uuid"]
        AU.create_device({
                "name" : name,
                "uuid" : uuid,
                "alias" : "",
                "listing" : [structure]
            })
        return 1
    except Exception as e:
        print(e)
        return 0

# @mutation.field("SignUp")
# def ql_SignUp(*_, account):
#     hashed = hashlib.md5(account["password"].encode()).hexdigest()
#     current: UserDetails = UserDetails(
#         None, f"{reClass.uuid.uuid4()}", account["email"], hashed, reClass.secrets.token_hex()
#     )
#     if not AU.user_database_query({"email": current.email}):
#         double_check = False
#         while double_check is not True:
#             if AU.user_database_query({"uuid": f"{current.uuid}"}) is None:
#                 double_check = True
#             current.uuid = f"{reClass.uuid.uuid4()}"
#         entry = UserDetailsSchema().dump(current)
#         AU.create_account(entry)
#         reClass.pprint(entry)
#         return entry
#     else:
#         return


# @query.field("Login")
# def ql_Login(*_, account):
#     current = UserDetails(
#         _id=None, uuid=None, email=account["email"], password=account["password"]
#     )
#     hashed = hashlib.md5(account["password"].encode()).hexdigest()
#     query = AU.user_database_query({"email": current.email})
#     if LoadedUsers().load(query).password != hashed:
#         return
#     if query is not None:
#         entry = LoadedUsers().load(query)
#         entry.password = account["password"]
#         entry = LoadedUsers().dump(entry)
#         return entry
#     else:
#         return


GraphQl = reClass.CreateSchema(SchemaString, [query, mutation])
