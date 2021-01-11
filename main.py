import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_number_10(num):
    total = 2
    for next_prime in get_primes(3):
        if next_prime < num:
            total += next_prime
        else:
            return (total)

# def prime_num(n):
#     for i in range(2, int(n//2) + 1):
#         if n % i == 0:
#             yield False
#     yield True

def main():
    # returns the sum of the prime numbers between 0 and num.
    # See jeffknupp blog on generators - really good explanation.

    num = int(input("Please enter the top range number: "))

    print("The sum of prime numbers to ", num, "is: ", solve_number_10(num))

if __name__ == '__main__':
    main()