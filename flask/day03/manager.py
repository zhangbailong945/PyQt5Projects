from flask import Flask
from flask_script import Manager
from App import create_app
from flask_migrate import MigrateCommand
import os

env=os.environ.get("FLASK_ENV","develop")

app=create_app(env)

manager=Manager(app=app)
manager.add_command('db',MigrateCommand)
if __name__ == "__main__":
    manager.run()
