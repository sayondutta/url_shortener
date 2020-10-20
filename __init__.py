from router import short
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(short)
    app.run()