from enum import Enum
from abc import ABC,abstractmethod

class BurgerTypes(Enum):
    CHEESE = "CHEESE"
    DELUXECHEESE = "DELUXECHEESE"
    VEGAN = "VEGAN"
    DELUXEVEGAN = "DELUXEVEGAN"

class Burger(ABC):

    def __init__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def get_name(self):
        return self.name

class BurgerStore(ABC):
    '''
    A Burger Store prepares burgers, based on Customer order
    A Customer will only input Order Type
    Burger Store takes BurgerType as an input and Prepares Burger using 
    Respective Burger class based on type.
    '''
    @abstractmethod
    def create_burger(self, burger_type:BurgerTypes) -> Burger:
        pass

    def order_burger(self, burger_type:BurgerTypes) -> Burger:
        '''

        '''
        burger = self.create_burger(burger_type)
        # using burger instance
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger

class CheeseBurger(Burger):
    def create_burger(self):
        super().__init__()
        self.name = "Cheese Burger"
        self.bread = "White Bread"
        self.sauce = "Chilli"
        self.toppings = ["Cheese", "Tomato"]
    
    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

    def get_name(self):
        return self.name

class DeluxeCheeseBurger(Burger):
    def create_burger(self):
        super().__init__()
        self.name = "Deluxe Cheese Burger"
        self.bread = "Wheat Bread"
        self.sauce = "Chilli"
        self.toppings = ["Double Cheese", "Tomato"]
    
    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

    def get_name(self):
        return self.name

class BurgerStoreCheese(BurgerStore):
    def create_burger(self, burger_type):
        if burger_type == BurgerTypes.CHEESE:
            return CheeseBurger()
        if burger_type == BurgerTypes.DELUXECHEESE:
            return DeluxeCheeseBurger() 
        return None

if __name__ == "__main__":
    cheese_store = BurgerStoreCheese()

    burger = cheese_store.order_burger(BurgerTypes.CHEESE)
    print(f"Ethan ordered a {burger.get_name()}")