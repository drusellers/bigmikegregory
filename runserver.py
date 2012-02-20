import os
from flask import Flask, render_template
from flaskext.assets import Environment, Bundle
import feedparser

app = Flask(__name__)
assets = Environment(app)
app.debug = True

app.config['LESS_PATH']='/usr/local/bin/lessc'

js = Bundle('scripts/jquery-1.7.1.min.js', filters='jsmin', output='scripts/gen.js')
assets.register('all-js', js)


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT","5000"))
    app.run(host='0.0.0.0',port=port)
