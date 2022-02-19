from flask import Flask
import auth
import blog
from db import initialize_db

app = Flask(__name__)
app.secret_key = 'super secret key'

app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

app.register_blueprint(auth.bp)
initialize_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
