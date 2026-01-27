from codelogger import log_performance, logger


class NumericProblems:
    @log_performance
    def sum_digits(self, num:int) -> int:
        result = 0
        while num > 0:
            last_digit = num % 10
            result += last_digit
            num = num // 10
        return result
    @log_performance
    def reverse_a_number(self, num:int) -> int:
        reversed_num = 0
        is_negative = num < 0
        logger.debug(f"initial number {num} and rev num {reversed_num}")
        while num > 0:
            last_digit = num%10
            logger.debug(f"last_digit {last_digit}")
            reversed_num = reversed_num * 10 + last_digit
            logger.debug(f"reversed_num {reversed_num}")
            num = num//10
            logger.debug(f"num {num}")
        return reversed_num
    

if __name__ == "__main__":
    res = NumericProblems()

    print(res.sum_digits(12345)) # 15
    print(res.reverse_a_number(12345)) # 54321