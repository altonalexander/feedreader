from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# for the current day's worth of tweets to read
# call xml/cleaned/filtered_health/besthealth/0
# call xml/original/filtered_health/besthealth/0 
@app.route('/xml/<feedcategory>/<feedname>/<source>/<int:daysago>')
@app.route('/xml/<feedcategory>/<feedname>')
def show_xml(feedcategory, feedname, source='cleaned', daysago='0'):
    result = 'XML for: Feed Category %s\n' % feedcategory
    result = result + 'Feed Name %s\n' % feedname
    result = result + '%d number of days ago\n' % int(daysago)
    result = result + 'Source %s\n' % source
    return result


# for all the word counts
@app.route('/entities/')
@app.route('/entities/<feedcategory>/')
@app.route('/entities/<feedcategory>/<feedname>/')
def show_entities(feedcategory='', feedname=''):
    result = 'ENTITIES in: Feed Category %s\n' % feedcategory
    result = result + 'Feed Name %s\n' % feedname
    return result

