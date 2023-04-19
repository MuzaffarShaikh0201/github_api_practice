from flask import request, json
from flask_restful import Resource
# dummy data
from data import data

class GithubApi(Resource):
    def post(self):
        if request.headers["Content-Type"] == "application/json":
            commits = request.json['commits']
            print(commits)
            print(type(commits))
            data.append(json.loads(commits))
            print(data)