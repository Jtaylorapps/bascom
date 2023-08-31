# Contains endpoints for the webapp

from flask import Flask, render_template, request, Response
from grabber import scrape_api
from http import HTTPStatus
import json
from datetime import datetime
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    """
    Basic endpoint for rendering the static index page
    """
    return render_template('index.html')

@app.route('/content/')
def content():
    """
    Endpoint for data/chart visualization page
    """
    # Create Bar chart
    fig = px.bar(pop_data,
                 labels={'year': 'Year', 'total_pop': 'Total Population'},
                 x='year', y='total_pop', height=600, width=1400)
    # Set chart color
    fig.update_traces(marker_color='rgb(21, 101, 192)', opacity=1)
    # fig.layout = Layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

    # Create graphJSON
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Use render_template to pass graphJSON to html
    return render_template('content.html',
                           title=f"Total Population of {country_name.upper()}",
                           graphJSON=graph_json,
                           last_updated=last_updated)

@app.route('/data/', methods=['POST'])
def data():
    """
    API endpoint for querying backend data with POST
    """
    year = request.form['inputYear']
    if year in pop_map:
        # Data exists, valid return
        return Response(json.dumps(pop_map[year]),status=HTTPStatus.OK,
                        mimetype='application/json')
    else:
        # Data does not exist, return an error
        return Response(json.dumps(f"Invalid year: {year}"),status=HTTPStatus.BAD_REQUEST,
                        mimetype='application/json')

if __name__ == '__main__':
    # Initialize data for the backend
    country_name = "us"  # Currently static, ideally configurable
    pop_map, pop_data = scrape_api(country_name)
    last_updated = datetime.now().strftime("%H:%M:%S")

    # Run server/keepalive
    app.config.from_object('config')
    app.run(host="0.0.0.0", port=80)

