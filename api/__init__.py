from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
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


api = Api()

def create_api(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/testdb'
    #CORS(app)
    from config import config
    try:
        init_config = config[config_name]
    except KeyError:
        raise
    except Exception:
        # For unforseen exceptionsayobussy8655
        raise
        exit()

    print('Running in {} Mode'.format(init_config))
    config_object = config.get(config_name)

    app.config.from_object(config_object)

    db.init_app(app)

    api.add_namespace(play_api, path='/play')

    api.init_app(app)
        
    incomes = [
    { 'description': 'salary', 'amount': 5000 }
    ]


    @app.route('/incomes')
    def get_incomes():
        return jsonify(incomes)


    @app.route('/incomes', methods=['POST'])
    def add_income():
        incomes.append(request.get_json())
        return '', 204
    return app