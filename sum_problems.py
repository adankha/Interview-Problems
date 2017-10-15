
def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    :param nums: list of nums
    :param target: target to find
    :return:
    """
    dict_vals = {}
    num_len = len(nums)

    for x in range(num_len):
        dict_vals[nums[x]] = x

    for y in range(num_len):
        new_target = target - nums[y]
        print(target, ' ', nums[y], ' ', target - nums[y])
        if new_target in dict_vals.keys() and dict_vals[new_target] != y:
            print(new_target)
            return [nums[y], target - nums[y]]


def three_sum(nums):
    """
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.
    :param nums:
    :return:
    """

    nums.sort()
    num_len = len(nums)
    res = []
    for left in range(num_len - 2):

        # Find duplicates: Since i is on the far left when walking,
        # If we don't handle this if-condition, then we are essentially going to have
        # duplicate triplets!
        if left > 0 and nums[left] == nums[left-1]:
            continue

        middle, right = left + 1, num_len - 1

        while middle < right:

            the_sum = nums[left] + nums[middle] + nums[right]
            if the_sum < 0:
                middle += 1
            elif the_sum > 0:
                right -= 1
            else:
                res.append((nums[left], nums[middle], nums[right]))
                # Skip any duplicate triplets when the middle iterator walks towards right
                while middle < right and nums[middle] == nums[middle+1]:
                    middle += 1
                # Skip any duplicate triplets when the right iterator walks towards middle
                while middle < right and nums[right] == nums[right-1]:
                    right -= 1
                middle += 1
                right -= 1
    return res


def main():

    s = [-1, 0, 1, 0]
    t = 3
    print('3-sum: ', three_sum(s))
    print('2-sum: ', two_sum(s, t))

    s = [-10, -3, -8, -3, 4, -1, -2, -4, -8, -5]
    t = 3
    print('\n3-sum: ', three_sum(s))
    print('2-sum: ', two_sum(s, t))

    s = [-1, 0, 1, 2, -1, -4]
    t = -5
    print('\n3-sum: ', three_sum(s))
    print('2-sum: ', two_sum(s, t))


if __name__ == '__main__':
    main()
