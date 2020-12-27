from http.client import responses


class Response:

    def __init__(
        self,
        body: str = '',
        status_code: int = 200,
        charset: str = 'utf-8'
    ):
        self._body: bytes = body.encode(charset)
        self._status_code: int = status_code
        self._charset: str = charset

    def __str__(self) -> str:
        return f"<class 'Response' {self.status_code}>"

    @property
    def body(self) -> bytes:
        return self._body

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def status_text(self) -> str:
        return responses.get(self.status_code, '')

    @property
    def status_message(self) -> str:
        return f'{self.status_code} {self.status_text}'
