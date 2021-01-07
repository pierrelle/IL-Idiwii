import spacy

from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

nlp = spacy.load("model/")

@app.route('/api/intent/sentence=<sentence>', methods=['GET'])
def get_intent(sentence):
    """
    file: Swagger.yml
    """
    result = nlp(sentence).cats
    return jsonify(result)