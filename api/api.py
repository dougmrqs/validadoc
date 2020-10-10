from flask import Flask

api = Flask(__name__)

from routes import *

api.config['DEBUG'] = True

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    api.run(host='0.0.0.0', port=5000)