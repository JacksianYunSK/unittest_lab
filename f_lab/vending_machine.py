
class DrinkMachine : 
    
    def __init__(self) -> None:
        self.credit = 0
        
    def insert_coin(self, coin):
        self.credit += coin
        
    def get_drink(self, drink):
        if self.credit > 0:
            self.credit = 0
            return drink
        else:
            return '돈을 넣어주세요'
        
    def get_drink_list(self):
        return ['콜라', '사이다', '환타']
    
        