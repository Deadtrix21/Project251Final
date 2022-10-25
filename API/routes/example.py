from flask import Blueprint
from flask import request, jsonify
from ariadne import gql, QueryType, MutationType, make_executable_schema, graphql_sync

class Main():
    def __init__(self):
        self.index = 3
        self.temp = []
        self.add_temp()

    def add_temp(self):
        self.temp = [
            {"name": "Paris", "description": "The city of lights",
            "country": "France", "ID": 0},
            {"name": "Rome", "description": "The city of pizza",
                "country": "Italy", "ID": 1},
            {
                "name": "London",
                "description": "The city of big buildings",
                "country": "United Kingdom",
                "ID": 2
            },
        ]

        
    def append_temp(self, name, description, country):
        object = {"name": name, "description": description, "country": country, "ID": self.index}
        self.temp.append(object)
        self.index += 1



type_defs = gql(
    """
    type Query {
        places: [Place]
    }


    type Place {
        name: String!
        description: String!
        country: String!
        ID:Int
    }

    type Mutation{
        add_place(name: String!, description: String!, country: String!): Place

        delete_field(id:String!): Int
    }
    """
)


# Initialize query

query = QueryType()

# Initialize mutation

mutation = MutationType()
MainApp = Main()

@query.field("places")
def places(*_):
    return MainApp.temp

# place resolver (add new  place)


@mutation.field("add_place")
def add_place(_, info, name, description, country):
    MainApp.append_temp(name, description, country)
    return {"name":name}


@mutation.field("delete_field")
def delete_field(_, info, id):
    print("a")
    return 0


schema = make_executable_schema(type_defs, [query, mutation])
user_api = Blueprint("userApi", __name__, )

@user_api.route('/users', methods=["GET"])
def shows():
    return "yes"


@user_api.route('/users', methods=["POST"])
def show():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code