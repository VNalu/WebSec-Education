from flask import request, Response
import requests
from . import app

SITE_NAME = 'http://juice-shop:3000/'
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def proxy(path):
    # print(f"Request: {request.__dict__}")
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, SITE_NAME),
        data=request.get_data(), 
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
            if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response

    
# resp = Request(recv_method, f'{SITE_NAME}{path}', 