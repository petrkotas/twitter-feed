from gevent.wsgi import WSGIServer
from twitter_feed import make_app


def main():
    http_server = WSGIServer(('', 5000), make_app())
    http_server.serve_forever()
