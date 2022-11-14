import hashlib

from core import reClass, DatabaseConnecting, DatabaseConnect

from models.user import LoadedUsers, UserDetails, UserDetailsSchema
from models.admin import LoadedAdmin, AdminDetails, AdminDetailsSchema
from models.device import LoadedDevice, DeviceDetails, DeviceDetailsSchema


from .schema import SchemaString

query = reClass.TQuery()
mutation = reClass.TMutation()


AU: DatabaseConnect = DatabaseConnecting


@query.field("echo")
def echo(*_, message):
    return {"msg": message}


@query.field("deviceGet")
def ql_deviceGet(*_, uuid):
    query = AU.device_database_query_many({"uuid": uuid})
    return query


@query.field("deviceGetAll")
def ql_deviceGetAll(*_):
    query = AU.device_database_query_many({})
    x = []
    for i in query:
        x.append(i)
    return x


@mutation.field("deviceDelete")
def ql_deviceDelete(*_, word):
    try:
        AU.device_database_del({"name": word})
        print(AU.device_database_query({"name": word}))
        return 1
    except Exception:
        return 0

    
@mutation.field("deviceLink")
def ql_deviceLink(*_, name, uuid):
    try:
        AU.device_database_update({"name": name}, {"uuid": uuid})
        return 1
    except Exception:
        return 0

@mutation.field("sectionAlias")
def ql_sectionAlias(*_, name, uuid, alias):
    try:
        AU.device_database_update({"name": name}, {"alias": alias})
        print(AU.device_database_query({"name": name}))
        return 1
    except Exception:
        print(3)
        return 0


@mutation.field("deviceUpdate")
def ql_deviceUpdate(*_, name, num, state):
    query = AU.device_database_query({"name": name})
    structure = {"level": state["level"],
                 "id": num, "current": state["current"]}
    print(query)
    try:
        if query != None:
            if "listing" not in query:
                raise EOFError
            entry = LoadedDevice().load(query)
            x, found = 0, False
            for i in entry.listing:
                if i["id"] == num:
                    found = True
                    query["listing"][x] = structure
                else:
                    pass
                x += 1
            if found == False:
                query["listing"].append(structure)
            AU.device_database_del({"name": name})
            AU.create_device(query)
            return 2
    except EOFError:
        uuid = ""
        if "uuid" in query:
            uuid = query["uuid"]
        AU.create_device(
            {"name": name, "uuid": uuid, "alias": "", "listing": [structure]}
        )
        return 1
    except Exception as e:
        print(e)
        return 0


GraphQl = reClass.CreateSchema(SchemaString, [query, mutation])
