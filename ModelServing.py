import spacy

from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

nlp = spacy.load("model/")

@app.route('/api/intent', methods=['GET'])
def get_intent():
    """
    file: Swagger.yml
    """
    sentence = request.args.get("sentence", None)
    result = nlp(sentence).cats
    return jsonify(result)