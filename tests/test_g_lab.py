import unittest

from g_lab.vending_machine import DrinkMachine

class TestLab(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_insert_coin(self):
        self.drink_machine = DrinkMachine()
        self.drink_machine.insert_coin(100)
        self.assertEqual(100, self.drink_machine.credit)
        
    def test_insert_coin_not_100(self):
        self.drink_machine = DrinkMachine()
        self.drink_machine.insert_coin(50)
        self.assertEqual(0, self.drink_machine.credit)
        
    def test_get_drink(self):
        self.drink_machine = DrinkMachine()
        self.drink_machine.insert_coin(100)
        self.assertEqual('콜라', self.drink_machine.get_drink('콜라'))
        self.assertEqual(0, self.drink_machine.credit)
    
    def test_get_drink_with_no_credit(self):
        self.drink_machine = DrinkMachine()
        self.assertEqual('돈을 넣어주세요', self.drink_machine.get_drink('콜라'))
        
    def test_get_drink_list(self):
        self.drink_machine = DrinkMachine()
        self.assertEqual(['콜라', '사이다', '환타'], self.drink_machine.get_drink_list())