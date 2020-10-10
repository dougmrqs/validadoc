from flask import Flask

api = Flask(__name__)

from routes import *

# api.config['DEBUG'] = True

if __name__ == "__main__":
    api.run()