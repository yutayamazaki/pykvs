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

    def test_get_default(self):
        ret: str = self.kvs.get('not exist', 'default')
        self.assertEqual(ret, 'default')

    def test_list(self):
        key: str = 'key'
        val: List[Any] = ['aa', 1, {'k': 'v'}]
        self.kvs.save(key, val)

        val_ = self.kvs.get(key)
        self.assertEqual(val, val_)

    def test_getitem(self):
        self.kvs['key2'] = 'value'
        self.assertEqual(self.kvs['key2'], self.kvs.get('key2'))


if __name__ == '__main__':
    unittest.main()
