import os
import shutil
import unittest
from typing import Any, Generator, List

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
        self.assertTrue(os.path.exists('./tests/pykvs/key.gz'))

        del self.kvs['key']
        self.assertFalse(os.path.exists('./tests/pykvs/key.gz'))

    def test_key_not_str(self):
        with self.assertRaises(TypeError):
            self.kvs.set(10, 'val')

    def test_keys(self):
        self.kvs['a'] = 'b'
        keys: List[str] = self.kvs.keys()
        self.assertEqual(keys, ['a'])

    def test_values(self):
        self.kvs['a'] = 'b'
        values: List[Any] = list(self.kvs.values())
        self.assertEqual(values, ['b'])

        values_gen = self.kvs.values()
        self.assertIsInstance(values_gen, Generator)

    def test_cache(self):
        self.kvs.set('key', 'Value', cache=True)
        self.assertEqual(self.kvs['key'], self.kvs.cache['key'])

    def test_cache_get(self):
        self.kvs.set('key', 'value', cache=False)
        self.kvs.get('key', cache=True)
        self.assertEqual(self.kvs.cache['key'], 'value')


if __name__ == '__main__':
    unittest.main()
