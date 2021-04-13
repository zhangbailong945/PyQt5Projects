
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app
import os

env=os.environ.get('develop') or 'default'

app=create_app(env)
manage=Manager(app=app)
manage.add_command('db',MigrateCommand)

if __name__=='__main__':
    manage.run()