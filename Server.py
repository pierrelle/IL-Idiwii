from ModelServing import IntentView

from flask import Flask, jsonify, request
from flasgger import Swagger

from waitress import serve

app = Flask(__name__)
swagger = Swagger(app)

app.add_url_rule(
    '/api/intent',
    view_func=IntentView.as_view('intent'),
    methods=['GET']
)

serve(app, host='0.0.0.0', port=8080)
