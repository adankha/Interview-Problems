"""
    PROBLEM: This problem was taken from leetcode.com

    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

    Given an encoded message containing digits, determine the total number of ways to decode it.

    For example,
        Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

        The number of ways decoding "12" is 2.


    Explanation of solution:
                {
                | We assume that leading character is not 0
                | dp[0] =>  1 base case
    dp[i][k] =  | dp[1] =>  1 since dp[0]
                | dp[i] =>  (dp[i-1] if 1 <= message[i - 1 : idx] <= 9)  + (dp[i-1] if 10 <= message[i - 2 : idx] <= 26)
                |   for i > 1
                {
                recurrence relationship explained:
                We are essentially looking at the previous digit. If it is between 1-9 inclusive
                we have a valid encoding.
                If we look at the last 2 digits, we check to see if it's between 10-26 inclusive.
                We then take the values stored in those positions and add it to the current position.

        Here we use Dynamic Programming to determine this. 

        Well, we know that there are 26 letters in the alpabet.
        With that said, we know that the letters A-Z can only map to digits that are 1 or 2 digits long.
        i.e.  A -> 1 and Z -> 26. This is very important for implementation!!!!

        Why is that important?

        We want to essentially walk through the string and evaluate every position.
        For every position, we evaluate the substring with length of 1, then
        substring of length 2.

        If the substring of length 1 has digits between 1-9 (since our mapping is 1-26, it can only be 1-9 inclusive),
        then we add to our array and hold the count for that index.

        We then evaluate length 2. The digits should only be 10-26 inclusive. For the same reason as above.
        So, 33 for example should only produce 1 way whereas 23 should produce 2 ways

        If at our current index we satisfy the conditions, we add the number of ways for those 2 substrings.

        We do this until we have reached the end of our string. The last element in our dp array holds the total number of ways.

        This can also be done just by using a few variables as opposed to using an array...
        That will help significantly with space complexity. (See num_decodings1(s))

        Note: Used leetcode explanations initially for some guidance as far as how to do this.
        So I cheated kinda, but I understand it fully! =)
        
        Why is DP beneficial here? Well, we are essentially building our number of decode ways from the previous.
        Anytime you build from the previous in the fashion as described it usually smells dynamic programming...

"""


def num_decodings1(s):

    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    prev1 = 1
    prev2 = 1
    result = 0

    for idx in range(2, len(s) + 1):

        # we reset result here because we want to always only add prev1 and prev2
        result = 0

        one_digit = int(s[idx - 1:idx])
        two_digit = int(s[idx - 2:idx])

        if 1 <= one_digit <= 9:
            result += prev1
        if 10 <= two_digit <= 26:
            result += prev2

        prev2 = prev1
        prev1 = result

    return result


def num_decodings2(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    dp = [0] * (len(s) + 1)

    dp[0] = 1
    dp[1] = 1

    for idx in range(2, len(s) + 1):

        one_digit = int(s[idx - 1:idx])
        two_digit = int(s[idx - 2:idx])

        if 1 <= one_digit <= 9:
            dp[idx] += dp[idx - 1]
        if 10 <= two_digit <= 26:
            dp[idx] += dp[idx - 2]

    return dp[len(s)]


def main():

    user_input = input('Enter any number: ')

    print('Number of ways: ', num_decodings1(user_input))
    print('Number of ways: ', num_decodings2(user_input))


if __name__ == '__main__':
    main()
