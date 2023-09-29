"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    number_to_test = 2
    if number_of_primes <= 0:
        raise ValueError
    while count < number_of_primes:
        for i in range(1, number_to_test) :
            if number_to_test % i == 0 and number_to_test != i and i != 1:
                number_to_test +=1
                continue
            elif i < number_to_test - 1: 
                continue 
            else:
                count += 1
                list.append(number_to_test)
                number_to_test +=1
                    
    return list