from flask_script import Manager, Server
from flask_script.commands import ShowUrls

from twitter_feed import make_app


manager = Manager(make_app)

manager.add_command("runserver", Server(host='0.0.0.0', port=5000))
manager.add_command('routes', ShowUrls())


@manager.shell
def make_shell_context():
    '''
    Prepare interactive shell to work with my app
    '''
    app = make_app()
    return dict(app=app)


@manager.command
def config():
    '''
    List sorted config options in the application
    '''
    with manager.app.app_context():
        for key in sorted(manager.app.config):
            print('{} : {}'.format(key, manager.app.config[key]))


if __name__ == "__main__":
    manager.run()
