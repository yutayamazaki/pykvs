import gzip
import os
import pickle
from typing import Any


class PyKVS:

    def __init__(self, path: str) -> None:
        self.path: str = path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get(self, key: str) -> Any:
        path: str = f'{self.path}/{key}'
        if not os.path.exists(path):
            return None
        with open(path, 'rb') as f:
            return pickle.loads(gzip.decompress(f.read()))

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def save(self, key: str, val: Any) -> None:
        path: str = f'{self.path}/{key}'
        with open(path, 'wb') as f:
            f.write(gzip.compress(pickle.dumps(val)))

    def __setitem__(self, key: str, val: Any) -> None:
        return self.save(key, val)
