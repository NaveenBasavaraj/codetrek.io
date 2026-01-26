class NumericProblems:
    def sum_digits(self, num:int) -> int:
        result = 0
        while num > 0:
            last_digit = num % 10
            result += last_digit
            num = num // 10
        return result
    
    def reverse_a_number(self, num:int) -> int:
        reversed_num = 0
        is_negative = num < 0
        while num > 0:
            last_digit = num%10
            reversed_num = reversed_num * 10 + last_digit
            num = num//10
        return reversed_num
    

if __name__ == "__main__":
    res = NumericProblems()

    print(res.sum_digits(12345)) # 15
    print(res.reverse_a_number(12345)) # 54321