import ModelServing

from waitress import serve

serve(ModelServing.app, host='0.0.0.0', port=8080)