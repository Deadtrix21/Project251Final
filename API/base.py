
class reClass:
    def __init__(self):
        pass

    # Flask API Define
    from flask import Flask
    from flask import request
    from flask import jsonify
    from flask import Blueprint

    # Graphql API Define
    from ariadne import gql as GraphqlString
    from ariadne import QueryType as TQuery
    from ariadne import MutationType as TMutation
    from ariadne import make_executable_schema as CreateSchema
    from ariadne import graphql_sync as SyncGraphql
    
    # DataClasses and MarshMellow
    import dataclasses
    import marshmallow

    # Others
    import os
    import json
    import numpy
    import uuid
    import datetime
    import secrets
app = reClass()
