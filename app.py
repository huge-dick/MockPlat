import os

from flask_cors import CORS
from flask import render_template
from flask_bootstrap3 import Bootstrap

import config
from exts import db
from kctool import kctool
from moco import moco
from re_flask import Flask

app = Flask(__name__)
CORS(app)

app.config.from_object(config)

app.register_blueprint(kctool,url_prefix='/kctool')
app.register_blueprint(moco,url_prefix='/')


app.secret_key = '123456'
bootstrap = Bootstrap(app)
COFIGPATH = os.path.join(os.getcwd(), 'moco/moco_file')

db.init_app(app)

@app.route('/restart')
def restart():
    return render_template('restart.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/http')
def http():
    return render_template('index.html')







if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
