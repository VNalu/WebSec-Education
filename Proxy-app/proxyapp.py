from flask import Flask, request
from requests import get

app = Flask(__name__)
SITE_NAME = 'http://juice-shop:3000/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  print(f"Request: {request.__dict__}")
  return get(f'{SITE_NAME}{path}').content