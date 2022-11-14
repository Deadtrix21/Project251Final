from core.base import reClass

SchemaString = reClass.GraphqlString(
    """
    type lists {
            id : Int
            current : String
            level : String
        
    }
    type info{
        alias   : String
        name    : String
        uuid    : String
        listing : [lists]
    }

    type Query {
        echo(message:String!) :String!
        deviceGet(uuid:String!): [info]!
        deviceGetAll:[info]
    }
    input Stats{
        current     : String!
        level       : String!
    }
    type Mutation{
        deviceUpdate(name:String!, num: String!, state: Stats!): Int
        devicesAdd(name:String!, uuid:String!): Int!
        sectionAlias(name:String!, uuid:String!, alias:String!): Int!

        deviceDelete(word:String!,):Int
        deviceLink(name:String!, uuid:String!):Int
    }
"""
)
