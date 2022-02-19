from flask import Flask
import auth
from db import initialize_db

app = Flask(__name__)
app.register_blueprint(auth.bp)
initialize_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
