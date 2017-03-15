from flask import Flask

from twitter_feed.config import config
from twitter_feed.views.rest import rest_view


def make_app(api=None):
    def before_request():
        '''
        Stuff to do before any request.
        Drop everything if not in endpoint.
        Check login.
        '''
        return

    # create the app and init the database with the app
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config.from_object(config.DevConfig)
    if api == 'dev':
        app.config['API'] = 'mock'

    app.before_request(before_request)

    app.register_blueprint(rest_view)

    return app
