import time


def method_4(n):
    """
    TODO::::
    Non-Lazy Sieve of Eratosthenes APPROACH
    :param n:
    :return:
    """

def method_3(n):
    """
    LAZY Sieve of Eratosthenes APPROACH

    Same idea as method 1, but we do it in a more clever way. We are essentially doing a "lazy"
    Sieve of Eratosthenes Algorithm.
    Here we are essentially just storing all the primes in a dictionary and then looping through those primes.
    This is similar to method 1, but we do some pruning as far as our inner-loop.

    Limitations: As mentioned above, since this is a lazy Sieve of Eratosthenes, we could do better by not having to
    loop through every single prime number each time.
    Instead what we can do is, once we find a prime number, we take that prime number and increment,
    prime_num += prime_num, and that new prime_num is not a prime num.
    Ex:
    prime_num = 2
    not_prime = 2

    not_prime += prime_num
    (now 4)
    4 not prime.
    not_prime += prime_num
    (now 6)
    6 not prime.
    We do this until we reach n, then stop. We then store these results and find the next number that we need to check.

    :param n: find all primes from 2 to n
    :return: return list of all primes up to n
    """
    res = []
    if n < 2:
        return res
    prime_dict = {}
    for i in range(2, n):
        is_prime = True
        for key in prime_dict.keys():
            if i % key == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
            prime_dict[i] = True
    return res


def is_prime_m2helper(n, i):
    """
    RECURSION HELPER

    Recursive helper for finding all primes
    :param n: Holds the current value we are evaluating
    :param i: i holds the current value we are evaluating outside the recursive call (the number we check if is prime)
    :return: boolean value if it is prime or not
    """
    if n == i:
        return True
    if i % n == 0:
        return False

    return is_prime_m2helper(n + 1, i)


def method_2(n):
    """
    RECURSION APPROACH

    Same idea as method 1 here but we do it recursively.
    We create an outer for-loop to test all prime numbers. So our outer loop, i is our "check if i is prime" variable
    The recursive call is our inner loop for "test if i is not modulos of any numbers up to i. If it is, not prime!
    :param n: Find all primes up to n
    :return: return list of all primes
    """

    res = []
    if n < 2:
        return res

    for i in range(2, n):
        if is_prime_m2helper(2, i):
            res.append(i)
    return res


def method_1(n):
    """
    ITERATIVE APPROACH

    This is done in an iterative approach.
    Idea: We traverse through in our 2nd loop from 2 to i-1 where i is our
    currently evaluated number. We check if i mod the j, where j = 2, 3, ..., i-1 is equal to 0
    if it is equal to 0, then we our number is not prime.

    Cons: We are evaluating every single number up to i which causes for major slowdown.
    We can use a dictionary to hold all current prime numbers and determine if a number is prime just by iterating
    with those numbers (see method3)

    :param n: Holds the n value to find all prime numbers to that num
    :return:
    """

    res = []
    if n < 2:
        return res

    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            res.append(i)
    return res


def main():

    user_input = input('Enter a number to find primes from 2-n: ')

    # Second Place
    # Test with primes to 25k numbers: 1560 ms
    st = time.time()
    res = method_1(int(user_input))
    et = time.time()
    print('\nMethod_1 (iterative)\nTime results: ', (et-st)*1000, 'ms\nList:', res)

    # Third Place
    # Test with primes to 25k numbers: breaks
    st = time.time()
    res = method_2(int(user_input))
    et = time.time()
    print('\nMethod_2 (recursion)\nTime results: ', (et-st)*1000, 'ms\nList:', res)

    # First Place
    # Test with primes to 25k numbers: 170 ms
    st = time.time()
    res = method_3(int(user_input))
    et = time.time()
    print('\nMethod_3 (Lazy Sieve of Eratosthenes)\nTime results: ', (et-st)*1000, 'ms\nList:', res)


if __name__ == '__main__':
    main()
