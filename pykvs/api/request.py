import urllib.parse
from typing import Any, Dict, List


class Request:

    def __init__(self, environ: Dict[str, Any]):
        self.environ = environ
        self.init(environ)

    def init(self, environ):
        self.method: str = environ.get('REQUEST_METHOD')
        self.path_info: str = environ.get('PATH_INFO')
        self.query_string: str = environ.get('QUERY_STRING')
        self.query_params: Dict[str, List[Any]] = urllib.parse.parse_qs(
            self.query_string
        )

    def __str__(self) -> str:
        return f"<class 'Request' {self.method}, {self.path_info}>"
