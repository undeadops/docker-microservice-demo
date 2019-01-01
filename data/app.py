## Data Access Layer
# This service will have a Mongo Dependency
from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Need to Fetch Mongo URL from etcd
mongo_client = MongoClient("mongodb://localhost:27017")

class MobyDockFeed(Resource):
    def put(self):
        print request.form['data']
        data = {
            "hostname":  'testy',
            "datetime": datetime.now()
            }
        print data
        results = mongo_client['MobyDock']['feeding'].insert(data)
        #TODO: Verify Insert...
        return { 'moby_status': 'Fed Krill to MobyDock' }

class MobyDock(Resource):
    def get(self):
        feeding_count = mongo_client['MobyDock']['feeding'].count ()
        return { 'feedings': feeding_count }

api.add_resource(MobyDockFeed, '/api/v1/feed/')
api.add_resource(MobyDock, '/api/v1/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
