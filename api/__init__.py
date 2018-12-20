from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_restplus import Api
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify, abort
from api.models import Bucketlist

play_api = Namespace('transaction', description='Api for dealing with every transaction happening in gtg')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

db = SQLAlchemy()
api = Api()

def create_api(config_name):
    app = Flask(__name__)
    #CORS(app)
    try:
        init_config = config[config_name]
    except KeyError:
        raise
    except Exception:
        # For unforseen exceptions
        raise
        exit()

    print('Running in {} Mode'.format(init_config))
    config_object = config.get(config_name)

    app.config.from_object(config_object)

    db.init_app(app)

    api.add_namespace(play_api, path='/play')

    api.init_app(app)
    
    @play_api.route('/bucketlists/', methods=['POST', 'GET'])
    def bucketlists():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            if name:
                bucketlist = Bucketlist(name=name)
                bucketlist.save()
                response = jsonify({
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'date_created': bucketlist.date_created,
                    'date_modified': bucketlist.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            bucketlists = Bucketlist.get_all()
            results = []

            for bucketlist in bucketlists:
                obj = {
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'date_created': bucketlist.date_created,
                    'date_modified': bucketlist.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app