from base import reClass

SchemaString = reClass.GraphqlString(
    """
    input LoginSignUp {
        email       :String!
        password    :String!
    }
    type UserDetails{
        email       : String!
        token       : String
    }
    type UserDetail{
        _id         : String!
        uuid        : String!
        email       : String!
        password    : String!
        token       : String
    }
    type Query {
        echo(message:String!) :String!
        Login(account:LoginSignUp):UserDetail
    }
    type Mutation{
        SignUp(account:LoginSignUp):UserDetails
    }
"""
)
