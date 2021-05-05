import flask
import json
import requests
import base64
from . import app

SITE_NAME = 'http://juice-shop:3000/'
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def proxy(path):
    # print(f"Request: {flask.request.__dict__}")
    req_data = flask.request.get_data() # To prevent weirdness from double call

    resp = requests.request(
        method=flask.request.method,
        url=flask.request.url.replace(flask.request.host_url, SITE_NAME),
        data=req_data, 
        headers={key: value for (key, value) in flask.request.headers if key != 'Host'},
        cookies=flask.request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection', 'x-frame-options']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
            if name.lower() not in excluded_headers]

    response = flask.Response(resp.content, resp.status_code, headers)

    # JSON to be sent to WebApp
    request_json = {
        "Session ID": 123, # TODO
        "Method": flask.request.method,
        "Host": flask.request.host,
        "Path": flask.request.path,
        "HTTP version": flask.request.environ.get("SERVER_PROTOCOL"),
        "Headers": {key: value for (key, value) in flask.request.headers},
        "Query String": flask.request.query_string.decode(),
        "Body": base64.b64encode(req_data).decode()
    }
    # request_json = json.dumps(request_json)
    
    # Make POST request to WebApp
    respToWebApp = requests.post(
        "http://web:5000/api/v1/request/new",
        data=request_json
    )

    return response

# TODO: sessionID maker function