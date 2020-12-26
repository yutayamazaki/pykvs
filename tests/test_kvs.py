import os
import shutil
import unittest
from typing import Any, List

import pykvs


class KVSTests(unittest.TestCase):

    def setUp(self):
        root: str = './tests/pykvs'
        if os.path.exists(root):
            shutil.rmtree(root)
        self.kvs = pykvs.PyKVS(root)

    def test_list(self):
        key: str = 'key'
        val: List[Any] = ['aa', 1, {'k': 'v'}]
        self.kvs.save(key, val)

        val_ = self.kvs.get(key)
        self.assertEqual(val, val_)
