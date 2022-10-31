from base import reClass
from .schema import SchemaString


query = reClass.TQuery()
mutation = reClass.TMutation()

def setupDetails(email, date, token):
    return {
        "email" : email,
        "expire": date,
        "token": token
    }

@query.field("echo")
def echo(*_, message):
    return message

@mutation.field("SignUp")
def ql_SignUp(*_, data):
    psw = data["password"]
    email = data["email"]
    if True:
        return setupDetails(email, "2020", reClass.secrets.token_hex())
    else:
        return "null"

@query.field("Login")
def ql_Login(*_, data):
    psw = data["password"]
    email = data["email"]
    if True:
        return setupDetails(email, "2020", reClass.secrets.token_hex())
    else:
        return "null"

GraphQl = reClass.CreateSchema(SchemaString, [query, mutation])