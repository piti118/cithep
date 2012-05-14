from cithep import *
from cithep.inipython import inipython
import unittest

class TestCithep(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_merge_dict(self):
        d1 = {'a':'b','c':'d'}
        d2 = {'e':'f','g':'h'}
        ret = merge_dict(d1,d2)
        for k,v in d1.items():
            self.assertIn(k,ret)
            self.assertEqual(v,ret[k])
            
        for k,v in d2.items():
            self.assertIn(k,ret)
            self.assertEqual(v,ret[k])

if __name__ == '__main__':
    unittest.main()
