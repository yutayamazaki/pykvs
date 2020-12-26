import gzip
import os
import pickle
from typing import Any


def _check_key(key: Any) -> None:
    if not isinstance(key, str):
        raise TypeError('key must be str.')


class PyKVS:

    def __init__(self, path: str) -> None:
        self.path: str = path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get(self, key: str, default: Any = None) -> Any:
        _check_key(key)

        path: str = f'{self.path}/{key}'
        if not os.path.exists(path):
            return default
        with open(path, 'rb') as f:
            return pickle.loads(gzip.decompress(f.read()))

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def set(self, key: str, val: Any) -> None:
        _check_key(key)
        path: str = f'{self.path}/{key}'
        with open(path, 'wb') as f:
            f.write(gzip.compress(pickle.dumps(val)))

    def __setitem__(self, key: str, val: Any) -> None:
        return self.set(key, val)

    def __delitem__(self, key: str) -> None:
        _check_key(key)
        path: str = f'{self.path}/{key}'
        os.remove(path)
