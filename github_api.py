from flask import request, json
from flask_restful import Resource
from data import data

class GithubApi(Resource):
    def post(self):
        if request.headers["Content-Type"] == "application/json":
            data.append(list(map(dict, request.json)))