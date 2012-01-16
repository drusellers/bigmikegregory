import os
from flask import Flask, render_template
from flaskext.assets import Environment, Bundle
import feedparser

app = Flask(__name__)
assets = Environment(app)
app.debug = True

app.config['LESS_PATH']='/usr/local/bin/lessc'

scss = Bundle('styles/main.less', filters='less', output='styles/base.css',
    debug=True)

assets.register('all-css', scss, output='styles/gen.css')


js = Bundle('scripts/jquery-1.7.1.min.js', filters='jsmin', output='scripts/gen.js')
assets.register('all-js', js)


def take(num, items):
    for i in range(num):
        yield items[i]

#blog posts - not sure codebetter has individual feeds
#posts = feedparser.parse('http://codebetter.com/drusellers/feed/').entries
#tweets
#tweets = feedparser.parse('http://twitter.com/statuses/user_timeline/drusellers.rss?count=10').entries
#github
#commits = feedparser.parse('https://github.com/drusellers.private.actor.atom?token=1dbb0464b79d688827f66a9120c32b10').entries
#wods?
#log = feedparser.parse('http://drusellers.tumblr.com/rss').entries

@app.route('/')
def hello():

    return render_template('index.html')
#            tweets=take(10, tweets),
#            commits=take(10, commits),
#            posts=take(10, posts),
#            log=take(10, log))


if __name__ == '__main__':
    port = int(os.environ.get("PORT","5000"))
    app.run(host='0.0.0.0',port=port)
