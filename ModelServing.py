import spacy
import logging
import time

from flask import Flask, jsonify, request
from flasgger import SwaggerView, Schema, fields

nlp = spacy.load("model/")

class IntentView(SwaggerView):
    parameters = [
        {
            "name": "sentence",
            "in": "query",
            "type": "string",
            "required": "true",
        }
    ]
    responses = {
        200: {
            "description": "Intents and their probabilities.",
        }
    }
    
    def get(self):
        sentence = request.args.get("sentence", None)
        
        start = time.time()
        result = nlp(sentence).cats
        end = time.time()
        
        logger = logging.getLogger("waitress")
        logger.setLevel(logging.INFO)
        logger.info(f" Process time: {end-start}")
        
        return jsonify(result)
