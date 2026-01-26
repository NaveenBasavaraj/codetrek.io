class EvenOdd:
    @staticmethod
    def is_even(num):
        return n%2==0
    
    @staticmethod
    def is_odd(num):
        return n%2 != 0
    
    @staticmethod
    def sum_of_evens_upto(num):
        return sum( n for n in range(2, num+1, 2))
    
    @staticmethod
    def sum_of_adds_upto(num):
        return sum( n for n in range(1, num+1, 2))
    
    @staticmethod
    def separate_even_and_odds(nums):
        