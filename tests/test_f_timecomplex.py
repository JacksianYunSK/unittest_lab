import unittest
import time

from f_timecomplex.main import all_combinations

class TestAllCombinations(unittest.TestCase):
    def test_large_input(self):
        large_list = list(range(20))  # 길이가 20인 리스트
        start_time = time.time()
        all_combinations(large_list)
        duration = time.time() - start_time
        self.assertTrue(duration < 1)  # 1초 이내에 완료되어야 함
    
    def test_short_input(self):
        large_list = list(range(5))  # 길이가 20인 리스트
        start_time = time.time()
        all_combinations(large_list)
        duration = time.time() - start_time
        self.assertTrue(duration < 1)  # 1초 이내에 완료되어야 함