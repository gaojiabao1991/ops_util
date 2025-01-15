# -*- coding: utf-8 -*-
import os, sys, re

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import unittest
from ops_util import *

class TestOpsUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self, *args, **kwargs):
        self.assertEqual(
            "abc",
            "abc"
        )



if __name__ == '__main__':
    unittest.main()