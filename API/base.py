import os

from dotenv import load_dotenv
from pymongo import MongoClient


class reClass:
    def __init__(self):
        pass

    import dataclasses
    import datetime
    import json
    import os
    import secrets
    import uuid

    import numpy
    from ariadne import MutationType as TMutation
    from ariadne import QueryType as TQuery
    from ariadne import gql as GraphqlString
    from ariadne import graphql_sync as SyncGraphql
    from ariadne import make_executable_schema as CreateSchema
    from dotenv import load_dotenv
    from flask import Blueprint, Flask, jsonify, request
    from marshmallow import (
        Schema,
        ValidationError,
        fields,
        post_dump,
        post_load,
        pprint,
        pre_dump,
        pre_load,
        validate,
        validates,
    )
    from pymongo import MongoClient


class database_handler:
    def __init__(self) -> None:
        self.connected = None
        self.connect()

    def get_cluster(self):
        try:
            if load_dotenv():
                return os.getenv("DATABASE")
        except Exception:
            print("No DataBase Key")

    def connect(self):
        self.connected = MongoClient(self.get_cluster(), serverSelectionTimeoutMS=5000)
        self.test_connection()

    def test_connection(self):
        try:
            self.connected.server_info()
            print("Connected")
        except Exception:
            print("Unable to connect to the server.")
