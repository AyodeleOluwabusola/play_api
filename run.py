import os
from api import create_api, db
from flask_migrate import Migrate
from os import environ

if environ.get('FLASK_ENV') is None:
    print('FLASK_ENV not set')
mode = environ.get('FLASK_ENV') or 'default'
app = create_api(mode)
migrate = Migrate(app, db)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5300)