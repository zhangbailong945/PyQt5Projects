from flask import Flask
from flask_script import Manager
app=Flask(__name__)

manager=Manager(app=app)

@app.route('/')
def index():
    a=10
    b=6
    c=0
    return '<p>hello world!</p>'

if __name__ == "__main__":
    manager.run()
