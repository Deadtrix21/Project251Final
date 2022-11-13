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
    type Query {
        Login(account:LoginSignUp):Admin
    }
"""
)
