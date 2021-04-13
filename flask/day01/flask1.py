from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    a=0
    b=3
    c=b/a
    return 'Hello World!%d'%c

if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')