from flask import Flask
from db import initialize_db

app = Flask(__name__)
initialize_db()


@app.route('/')
def hello_world(): 
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
