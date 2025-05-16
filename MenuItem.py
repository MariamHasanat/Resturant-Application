from Restaurant import Restaurant

class MenuItem:
    
    def __init__(self, name: str, price: float = 0, category: str = ""):
        self.__name = name
        self.__price = price
        self.__category = category

    def set_name(self, name: str):
        self.__name = name
    
    def set_price(self, price: float):
        self.__price = price
    
    def set_category(self, category: str):
        self.__category = category
        
    def get_name(self) -> str:
        return self.__name
    
    def get_price(self) -> float:
        return self.__price
    
    def get_category(self) -> str:
        return self.__category