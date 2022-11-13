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

class DatabaseConnect:
    def __init__(self) -> None:
        self.__db = None
        self.__autoconnect()

    def __autoconnect(self):
        self.__db = database_handler().connected

    def __get_database(self, arg: str) -> reClass.MongoClient:
        arg = arg.lower()
        switch_case = {
            "user": self.__db["Project251"]["Users"], 
            "admin": self.__db["Project251"]["Admins"],
            "device": self.__db["Project251"]["Devices"],
            }
        return switch_case.get(arg, None)

    def user_database_query(self, query, exclude=None):
        user = self.__get_database("user")
        res = None
        if exclude is None:
            res = user.find_one(query)
        else:
            res = user.find_one(query, **exclude)
        return res

    def admin_database_query(self, query, exclude=None):
        user = self.__get_database("admin")
        res = None
        if exclude is None:
            res = user.find_one(query)
        else:
            res = user.find_one(query, **exclude)
        return res
    
    def device_database_query(self, query, exclude=None):
        user = self.__get_database("device")
        res = None
        if exclude is None:
            res = user.find_one(query)
        else:
            res = user.find_one(query, **exclude)
        return res
    
    def device_database_query_many(self, query, exclude=None):
        user = self.__get_database("device")
        res = None
        if exclude is None:
            res = user.find(query)
        else:
            res = user.find(query, **exclude)
        return res
    

    def device_database_update(self, what, query):
        user = self.__get_database("device")
        try:
            user.update_one(what, {"$set": query})
            return 1
        except Exception:
            return 0

    def device_database_del(self, query):
        user = self.__get_database("device")
        res = user.delete_one(query)

    def create_account(self, data):
        user = self.__get_database("user")
        user.insert_one(data)

    def create_device(self, data):
        user = self.__get_database("device")
        user.insert_one(data)
