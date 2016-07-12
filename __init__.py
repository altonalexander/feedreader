import boto3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# config
@app.route('/config/')
@app.route('/config/<file>')
def show_config(file='feeds.json'):
    filename = 'rob_princetonventures'
    filename = filename + '/feeds.json'

    # get the preprocessed file from s3
    s3 = boto3.resource('s3')
    object = s3.Object('com.frontanalytics.feedreader',filename)
    result = object.get()["Body"].read()
    return result


# for the current day's worth of tweets to read
# call feed/filtered_health/besthealth
@app.route('/feed/<feedcategory>/<feedname>/')
def show_xml(feedcategory, feedname, source='cleaned', daysago='0'):
    filename = 'rob_princetonventures'
    if ( feedcategory!='' ):
        filename = filename+'/%s' % feedcategory
    if ( feedname!='' ):
        filename = filename+'/%s' % feedname
    filename = filename + '/cleaned_latest.xml'

    # get the preprocessed file from s3
    s3 = boto3.resource('s3')
    object = s3.Object('com.frontanalytics.feedreader',filename)
    result = object.get()["Body"].read()
    return result


# return the log
@app.route('/log/')
@app.route('/log/<feedcategory>/')
@app.route('/log/<feedcategory>/<feedname>/')
def show_log(feedcategory, feedname, source='cleaned', daysago='0'):
    filename = 'rob_princetonventures'
    if ( feedcategory!='' ):
        filename = filename+'/%s' % feedcategory
    if ( feedname!='' ):
        filename = filename+'/%s' % feedname
    filename = filename + '/log.html'

    # get the preprocessed file from s3
    s3 = boto3.resource('s3')
    object = s3.Object('com.frontanalytics.feedreader',filename)
    result = object.get()["Body"].read()
    return result

# for all the word counts
@app.route('/entities/')
@app.route('/entities/<feedcategory>/')
@app.route('/entities/<feedcategory>/<feedname>/')
def show_entities(feedcategory='', feedname=''):

    # create the filename
    filename = 'rob_princetonventures'
    if ( feedcategory!='' ):
	filename = filename+'/%s' % feedcategory
    if ( feedname!='' ):
	filename = filename+'/%s' % feedname
    filename = filename + '/entities.csv'

    # get the preprocessed file from s3
    s3 = boto3.resource('s3')
    object = s3.Object('com.frontanalytics.feedreader',filename)

    result = object.get()["Body"].read()

    return result



if __name__ == "__main__":
    app.run()
