from core.base import reClass

SchemaString = reClass.GraphqlString(
    """
    input LoginSignUp {
        email       :String!
        password    :String!
    }

    type Admin{
        uuid        : String!
        token       : String!
    }
    type UserDetail{
        _id         : String!
        uuid        : String!
        email       : String!
        password    : String!
        token       : String
    }
    type Query {
        Login(account:LoginSignUp):Admin
        Users:[UserDetail]
    }
"""
)
