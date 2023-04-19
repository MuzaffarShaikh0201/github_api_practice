from flask import request, json
from flask_restful import Resource
from data import data

class GithubApi(Resource):
    def post(self):
        if request.headers["Content-Type"] == "application/json":
            commits = request.json['commits'][0]
            data.append(list(map(dict, commits)))
            print(commits)
            print(data)