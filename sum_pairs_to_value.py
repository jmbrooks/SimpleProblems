"""
Given a list and a desired sum, find pairs in the list that sum to that value.
"""
def has_sum_pair(input_list: list, sum: int) -> list:
    """Given list and desired integer sum, determines if a pair sums to that value."""
    complement_set = set()
    for number in input_list:
        if (sum - number) in complement_set:
            return [True, [number, sum - number]]
        complement_set.add(number)
    return [False, []]


input_list = [1, 9, 3, 6, 7, 4, 4]
input_list_2 = [2, 5, 5, 1, 2, 6, 4]
input_list_3 = []

print(has_sum_pair(input_list, 22))
print(has_sum_pair(input_list_2, -5))
print(has_sum_pair(input_list_3, 2))
