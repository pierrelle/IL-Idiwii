import spacy

from flask import Flask

app = Flask(__name__)

nlp = spacy.load("model/")

@app.route('/api/intent/sentence=<sentence>', methods=['GET'])
def get_intent(sentence):
    return nlp(sentence).cats