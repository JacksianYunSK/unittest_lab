import unittest
import a_tutorial.main as main

class TEST_MAIN(unittest.TestCase) : 
    def test_sum_func(self) : 
        ret = main.sum(5,7)
        self.assertEqual(12,ret)
        
        