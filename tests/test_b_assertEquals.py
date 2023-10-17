# unittest를 이용하여 테스트를 진행할 수 있습니다. 
# unittest.TestCase를 상속받은 클래스를 만들고,
# test_로 시작하는 함수를 만들어서 테스트를 진행합니다.
# main.py 에 있는 함수들을 테스트하는 코드를 만들어 봅니다. 

import unittest
import b_assertEquals.main as main

class Test_main(unittest.TestCase) : 
    def test_foo_func(self) : 
        ret = main.foo(10,5)
        self.assertEqual(2,ret)
        
    def test_bar_func(self) : 
        ret = main.bar(10,5)
        self.assertEqual(50,ret)
        
    def test_sum_func(self) : 
        ret = main.sum(10,5)
        self.assertEqual(15,ret)
        
    def test_sub_func(self) : 
        ret = main.sub(10,5)
        self.assertEqual(5,ret)
        
    # 만약 정수가 아닌 소수가 있는 값이 들어오는 경우에 대한 테스트도 해보겠습니다.

    def test_foo_func_temp(self) :
        ret = main.foo(10,3)
        self.assertEqual(3.333, ret)
    

    # 이 경우에는 assertAlmostEqual를 사용합니다.
    # assertAlmostEqual는 두 값이 거의 같은지를 테스트합니다.
    
    def test_foo_func_1(self) :
        ret = main.foo(10,3)
        self.assertAlmostEqual(3.333, ret, places = 3)
        
    def test_bar_func_1(self) :
        ret = main.bar(10,3.333333)
        self.assertAlmostEqual(33.333, ret, places = 3)
    
    
    # 하지만 위 테스트에서 하나 간과된게 있습니다. 
    # 0으로 나누는 경우에 대한 테스트가 없습니다.
    # 이런 경우에는 assertRaises를 사용합니다.
    # assertRaises는 예외가 발생하는지를 테스트합니다.

    def test_foo_func_2(self) :
        self.assertRaises(ZeroDivisionError, main.foo, 10, 0)
        
    # 그 외에도 다양한 예외를 테스트할 수 있습니다.
    # 만약 정수가 아닌 값이 들어오는 경우에 대한 예외도 확인해 볼 수 있습니다. 
    
    def test_foo_func_3(self) :
        self.assertRaises(TypeError, main.foo, 10, 'a')
        
        