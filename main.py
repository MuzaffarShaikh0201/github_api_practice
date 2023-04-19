from flask import Flask
from flask_restful import Api
from home import Home
from github_api import GithubApi

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(GithubApi, '/github_api')

if __name__ == "__main__":
    app.run(port=5000, debug=True)