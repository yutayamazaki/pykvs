import glob
import gzip
import os
import pickle
from typing import Any, List


def _check_key(key: Any) -> None:
    if not isinstance(key, str):
        raise TypeError('key must be str.')


class PyKVS:

    def __init__(self, root: str) -> None:
        self.root: str = root
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def get(self, key: str, default: Any = None) -> Any:
        _check_key(key)

        path: str = f'{self.root}/{key}.gz'
        if not os.path.exists(path):
            return default
        with open(path, 'rb') as f:
            return pickle.loads(gzip.decompress(f.read()))

    def set(self, key: str, val: Any) -> None:
        _check_key(key)
        path: str = f'{self.root}/{key}.gz'
        with open(path, 'wb') as f:
            f.write(gzip.compress(pickle.dumps(val)))

    def keys(self) -> List[str]:
        keys: List[str] = []
        for path in glob.glob(f'{self.root}/*.gz'):
            key, _ = os.path.splitext(os.path.basename(path))
            keys.append(key)
        return keys

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def __setitem__(self, key: str, val: Any) -> None:
        return self.set(key, val)

    def __delitem__(self, key: str) -> None:
        _check_key(key)
        path: str = f'{self.root}/{key}.gz'
        os.remove(path)
