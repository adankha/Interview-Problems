"""

PROBLEM: Create a program that finds the nth fibonacci number in a fibonacci sequence.


The following program demonstrates how to solve Fibonacci in two different ways:

    1) Recursively using non DP
    2) Using Dynamic Programming

    Time-Complexity is shown to demonstrate the differences between the two.

    Essentially 1) goes over a lot of the same numbers it has already visited. That is why DP is useful here!

    Note: 2) is good because you hold all fibonacci numbers up to the number the user enters.
    If you want to find a different fibonacci number < the one user initially entered in,
    then you have O(1) access, whereas in method 1) you have to iterate through recursively.

    Note: Fibonacci is a perfect example of using Dynamic Programming!!

    Used Python 3.6.2

"""

import time


def r_fibonacci(n):
    if n <= 1:
        return n
    return r_fibonacci(n-1) + r_fibonacci(n - 2)


def dp_fibonacci(n):

    dp = [0]*(n+1)

    dp[0] = 0
    dp[1] = 1

    for idx in range(2, n+1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    return dp[idx]


def main():

    user_input = input('\nEnter the sequence number for the fibonacci sequence: ')

    print('\nFinding fibonacci number at', user_input, 'using recursion and dp...\n\n')

    start_time = time.time() * 1000.0
    print('The fibonacci number at', user_input, 'is:', r_fibonacci(int(user_input)), 'using recursion.')
    end_time = time.time() * 1000.0
    print('Recursion Time: ', (end_time - start_time), 'ms\n\n')

    start_time = time.time() * 1000.0
    print('The fibonacci number at', user_input, 'is:', dp_fibonacci(int(user_input)), 'using dp.')
    end_time = time.time() * 1000.0
    print('Dynamic Programming Time: ', (end_time - start_time), 'ms')


if __name__ == '__main__':
    main()
