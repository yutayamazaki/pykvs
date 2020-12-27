import json
from typing import Any, Callable, Dict, List
from wsgiref import simple_server

import pykvs
from pykvs.api.request import Request
from pykvs.api.response import Response

kvs = pykvs.PyKVS('./kvs_storage')


def pykvs_app(environ: Dict[str, Any], start_response: Callable):
    request: Request = Request(environ)

    resp: Response = Response('Error\n', status_code=400)

    if request.method == 'GET' and request.path_info == '/kvs':
        resp = get_kvs(request)

    if request.method == 'POST' and request.path_info == '/kvs':
        resp = set_kvs(request)

    start_response(resp.status_message, [('Content-type', 'application/json')])
    return [resp.body]


def get_kvs(request: Request) -> Any:
    params: Dict[str, List[Any]] = request.query_params
    key: str = params['key'][0]
    value: Any = kvs[key]
    return Response(json.dumps({'value': value}), status_code=200)


def set_kvs(request: Request) -> Any:
    params: Dict[str, List[Any]] = request.query_params
    key: str = params['key'][0]
    value: Any = params['value'][0]
    kvs[key] = value
    return Response(json.dumps({'key': key, 'value': value}), status_code=200)


class API:

    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host: str = host
        self.port: int = port

    def run(self):
        server = simple_server.make_server(self.host, self.port, pykvs_app)
        print(f'Running server on http://{self.host}:{self.port}')
        server.serve_forever()
