import os
import shutil
import unittest
from typing import Any, List

import pykvs


class KVSTests(unittest.TestCase):

    root: str = './tests/pykvs'

    def setUp(self):
        self.kvs = pykvs.PyKVS(self.root)

    def tearDown(self):
        if os.path.exists(self.root):
            shutil.rmtree(self.root)

    def test_get_default(self):
        ret: str = self.kvs.get('not exist', 'default')
        self.assertEqual(ret, 'default')

    def test_list(self):
        key: str = 'key'
        val: List[Any] = ['aa', 1, {'k': 'v'}]
        self.kvs.set(key, val)

        val_ = self.kvs.get(key)
        self.assertEqual(val, val_)

    def test_getitem(self):
        self.kvs['key2'] = 'value'
        self.assertEqual(self.kvs['key2'], self.kvs.get('key2'))

    def test_delitem(self):
        self.kvs['key'] = 'value'
        self.assertTrue(os.path.exists('./tests/pykvs/key'))

        del self.kvs['key']
        self.assertFalse(os.path.exists('./tests/pykvs/key'))

    def test_key_not_str(self):
        with self.assertRaises(TypeError):
            self.kvs.set(10, 'val')


if __name__ == '__main__':
    unittest.main()
