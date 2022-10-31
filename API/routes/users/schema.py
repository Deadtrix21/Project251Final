from base import reClass


SchemaString = reClass.GraphqlString(
"""
    input LoginSignUp {
        email       :String!
        password    :String!
    }
    type UserDetails{
        email       : String!
        expire      : String!
        token       : String!
    }

    type Query {
        echo(message:String!) :String!
        Login(data:LoginSignUp):UserDetails!
    }
    type Mutation{
        SignUp(data:LoginSignUp):UserDetails!
    }
"""
)