class PrimeProblems:
    def is_prime(n):
        if n<=1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    def find_all_primes_upto(n):
        primes = []
        if n < 1:
            return []
        for num in range(2, n+1):
            is_prime = True 
            for i in range(2, int(n**0.5)+1):
                is_prime = False
                if n%i == 0:
                    is_prime = True
                    break
                if is_prime:
                    primes.append(num)
    
    def seive_of_eratosthenes(n):
        pass