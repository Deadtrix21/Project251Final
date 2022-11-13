from core.base import reClass

SchemaString = reClass.GraphqlString(
    """
    type Query {
        echo(message:String!) :String!
        deviceGet(uuid:String!): []!
    }

    input Stats{
        current     : Int!
        level       : String!
    }
    type Mutation{
        deviceUpdate(name:String!, num: Int!, state: Stats!): Int
        devicesAdd(name:String!, uuid:String!): Int!
    }
"""
)
