import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            # 'cnn': 'http://rss.cnn.com/rss/edition.rss',
            # 'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}

# @app.route('/')
# @app.route('/bbc')
# def bbc():
#     return get_news('bbc')
#
# @app.route('/iol')
# def cnn():
#     return get_news('iol')

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    # first_artice = feed['entries'][0]
    # return """<html>
    #   <body>
    #       <h1> BBC Headlines </h1>
    #       <b>{0}</b> <br/>
    #       <i>{1}</i> <br/>
    #       <p>{2}</p> <br/>
    #   </body>
    # </html>
    # """.format(first_artice.get("title"), first_artice.get("published"), first_artice.get("summary"))
    # return render_template('home.html',
    #                        title=first_artice.get('title'),
    #                        published=first_artice.get('published'),
    #                        summary=first_artice.get('summary'))
    # return render_template('home.html', article=first_artice)
    return render_template('home.html', articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)

