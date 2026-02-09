class EvenOdd:
    @staticmethod
    def is_even(num):
        return num%2==0
    
    @staticmethod
    def is_odd(num):
        return num%2 != 0
    
    @staticmethod
    def sum_of_evens_upto(num):
        return sum( n for n in range(2, num+1, 2))
    
    @staticmethod
    def sum_of_adds_upto(num):
        return sum( n for n in range(1, num+1, 2))
    
    @staticmethod
    def separate_even_and_odds(nums):
        even = list(filter(lambda x:x%2==0, nums))
        odd = list(filter(lambda x:x%2!=0, nums))
        return f"even {even} and odd {odd}"
    
if __name__ == "__main__":
    res = EvenOdd()
    print(res.separate_even_and_odds([1,2,3,4,5,6,7,8]))
        