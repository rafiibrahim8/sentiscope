from flask import Blueprint, request
import os

from ...ml import SentimentAnalyzer
from ...utils import get_logger

MODEL_NAME = 'finiteautomata/bertweet-base-sentiment-analysis'

this_path = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.normpath(os.path.join(
    this_path, '..', '..', '..', 'model'))
model_basename = os.path.basename(MODEL_NAME)

if os.path.exists(os.path.join(model_dir, model_basename)):
    get_logger().info('Using local model.')
    model_path = os.path.join(model_dir, model_basename)
else:
    get_logger().info('Using remote model. This may download the model if not cached.')
    model_path = MODEL_NAME

seniment_analyzer = SentimentAnalyzer(model_path)
get_logger().info('Loading ML model... This may take a while.')
seniment_analyzer.load_model()

blueprint = Blueprint('v1', __name__, url_prefix='/v1')


def get_sentiment(text):
    return seniment_analyzer.get_sentiment(text)


@blueprint.post('/analyze')
def analyze():
    data = request.get_json()
    if not isinstance(data, dict):
        return {'error': 'Invalid payload'}, 400
    if 'text' not in data:
        return {'error': 'Invalid payload'}, 400
    return get_sentiment(data['text']), 200
