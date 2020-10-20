import sys
sys.path.append('app/')
from router import short
from flask import Flask

app = Flask(__name__)
app.register_blueprint(short)