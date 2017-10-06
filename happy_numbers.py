"""
    PROBLEM: Find all the happy numbers between 1 and n.

    What is a happy number? Gr8 question m8...

    Given a number n = n_0, define a sequence n_1, n_2, ... where n_i+1 is the sum of the squares of the digits of n_i
    A number n is happy if and only if there exists an i such that n_i = 1.

    A happy number is happy if all members of its sequence are happy.
    If a number is unhappy, all members of the sequence are unhappy.

    What the hell does all of this mean? Lets see an example, thx wikipedia:

        19 is a happy number!

        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

        Since we landed on 1, we're happy!


    Explanation of solution:
        Our goal is to take the number currently evaluated, break up all the sub numbers in that number,
        square the sub numbers,
        add them together,
        check to see if they are equal to 1.

        We do this simply by using some mathematical rules of mod. If we take modulus 10 of the number
        We will get the last integer value of that number. So 82 % 10 = 2, 3 % 10 = 3, 175928 % 10 = 8.
        This modulus technique gets us the last number.
        Now our goal is to traverse through the number being evaluated and get each sub-number (has to be 0-9)
        To do this we divide the curr_number by 10 and store curr_numb to be the result.
        We divide by 10 each time because it allows us to get the tens place for each num

        ex: 1234

        1234 / 10 = 123.4
        123 / 10 = 12.3
        12 / 10 = 1.2
        1 / 10 = 0
        (cast as int)

        This helps us get each sub number in our number.

        We then square each number, add it to a total then check for the total.

        If total is 1, we are done, it's happy (By definition of happy number)

        Otherwise, we recursively pass the total number into our function and evaluate that next sequence number.

        If our total result loops back to a number we've already found before, then we have an infinite loop.

        Infinite loop = not good = not a happy number.

        We store each value in a dictionary to check for this re-visit.

        So we return false... However, since we are dealing with sequences we know that if a number is happy or unhappy
        then all the numbers to get to that number is happy or unhappy as well...

        Knowing this implies that we can use some sort of banking mechanism to improve run-time.

        So if we are trying to evaluate if a number is happy, we want to have a global dictionary that holds all of our
        previous results so that we don't do the same calculations. <--- This is memoization!


        ...
        n by 10^# of iterations


"""
from copy import deepcopy
import time


def is_happy(n, local_dict, global_dict):

    curr_num = deepcopy(n)
    total = 0

    if n == 0:
        return False
    if n == 1:
        return True

    if n in global_dict.keys():
        return global_dict[n]

    local_dict[n] = False

    while curr_num != 0:
        total += (curr_num % 10) * (curr_num % 10)
        curr_num = int(curr_num / 10)
    if total == 1:
        return True
    elif total in local_dict.keys():
        return False
    else:
        local_dict[total] = is_happy(total, local_dict, global_dict)
        return local_dict[total]


def main():

    user_input = input('Enter a number to find all happy numbers up to that number: ')

    local_dict = {}
    global_dict = {}
    happy_list = []

    # Not using Memoization
    start = time.time() * 1000
    for idx in range(1, int(user_input)):

        result = is_happy(idx, local_dict, global_dict)

        if result:
            global_dict[idx] = True
            happy_list.append(idx)
        else:
            global_dict[idx] = False
        local_dict.clear()

    end = time.time() * 1000
    print('Time taken with  memoization: ', end - start, 'ms')

    happy_list.clear()
    global_dict.clear()

    # Using Memoization
    start = time.time() * 1000
    for idx in range(1, int(user_input)):
        result = is_happy(idx, local_dict, global_dict)
        if result:
            happy_list.append(idx)
        local_dict.clear()

    end = time.time() * 1000

    print('Time taken w/out Memoization: ', end - start, 'ms')
    print('The happy numbers:', happy_list)


if __name__ == '__main__':
    main()
