from flask import Flask, render_template
import json
from datetime import datetime

with open('data.json') as f:
    data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now()
    for collection in data:
        collection_date = datetime.strptime(collection['date'], '%d/%m/%Y')
        if collection_date >= today:
            next_collection = collection
            break

    # Handle more than one bin
    if '_' in next_collection['colour']:
        multiple_bins = True
        next_collection['colour'] = next_collection['colour'].replace('_', ' and ')
    else:
        multiple_bins = False

    return render_template('index.html', date=next_collection['date'], colour=next_collection['colour'], multiple_bins=multiple_bins)

if __name__ == '__main__':
    app.run(debug=True)
