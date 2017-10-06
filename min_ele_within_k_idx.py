"""
    PROBLEM: For each index, find the min element within k-indices prior to that index.

    What does that mean?

    Lets maybe look at an example...

    Let k = 3

    idx:    [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
    values: [6,  7,  8, 12,  3,  2,  1, 17, 18,  5,  9]

    We want to check the minimum element within k indices from our currently evaluated index.

    So our results:
    idx:    [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
    result: [N,  6,  6,  6,  7,  3,  2,  1,  1,  1, 17]

    How do we accomplish this task?

    We can use a modified version of the Knapsack problem to do this.

    Lets create a 2d array where we have n x k.

    From there we can utilize some known minimums with our previous indices to determine our currently evaluated
    index.

    How?

    Let k = 3:

    key(our value): k vals[1-k]

    idx:  val:  k =  1,    2,   3
    0    [6]  : [none, none, none]
    1    [7]  : [6, 6, 6]
    2    [8]  : [7, 6, 6]
    3    [12] : [8, 7, 6]
    4    [3]  : [12, 8, 7]
    5    [2]  : [3, 3, 3]
    6    [1]  : [2, 2, 2]
    7    [17] : [1, 1, 1]
    8    [18] : [17, 1, 1]
    9    [5]  : [18, 17, 1]
    10   [9]  : [5, 18, 17]

    Notice the pattern? For our current evaluated index, When k = 1, it has to be the number next to our evaluated index
    When k = 2, we take whatever the min is of our previous index at k = 1
    When k = 3, we take whatever the min is of our previous index at k = 2

    When finished, our last elements of each row holds the min.

"""


# TODO Finish algo
def create_knapsack(arr, k):

    knapsack = []

    return knapsack


def main():

    arr = [6, 7, 8, 12, 3, 2, 1, 17, 18, 5, 9]
    k = 3

    result = create_knapsack(arr, k)
    print('The Knapsack Result: ', result)


if __name__ == '__main__':
    main()