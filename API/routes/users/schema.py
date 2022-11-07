from base import reClass

SchemaString = reClass.GraphqlString(
    """
    input LoginSignUp {
        email       :String!
        password    :String!
    }
    type Token {
        expire : String
        token : String
    }
    type UserDetails{
        email       : String!
        token       : Token!
    }
    type UserDetail{
        _id         : String!
        uuid        : String!
        email       : String!
        password    : String!
        token       : Token!
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
