# Given an increasingly sorted array and a number s, please find two numbers
# whose sum is s. If there are multiple pairs with sum s, just output any one of
# them.

# For example, if the inputs are an array {1, 2, 4, 7, 11, 15} and a number 15,
# please out two numbers 4 and 11 since 4+11=15.

# Iteratively find substets from given array and add them up as we go and
# compare with the given value

# BONUS: Do the same as above, but instead of a sum, find the product one!
# (given an array of 100 numbers, get the two numers whose product will give you
# a third number given.
# it can be done with O(n) space and O(n) Runtime with Hash.
# 
# Step#1 Iterate over Array.
# Step#2 Key = 30/Array[i]. 
#         a)Check if the key exists in Hashmap. If yes, print key and Array[i]
#         b)if not [Insert key into Hashmap ]

def summed_pair(arr):
    # The last number to check is going to be always smaller than num
    start = 0
    end = len(arr)-1

    while arr[end] >= num:
        end -= 1

    j = 0
    for i in arr:
        while j <= end:
            aux = arr[i] + arr[j]
            if aux == num:
                return arr[i], arr[j]
            j += 1
    return None

#thiago's solution
a = [1, 3, 4, 5, 6, 7, 11, 15]
def has_two_numbers_sum(a, n):
    if len(a) <= 1:
        return None

    small = 0
    big = len(a)-1

    while arr[big] >= num:
        big -= 1
    while small < big:
        currSum = a[small] + a[big]
        if currSum == n:
            return a[small], a[big]
        else:
            if currSum > n:
                big -= 1
            else:
                small += 1
    return None

#part 1
print('part 1')
print(has_two_numbers_sum(a, 15))
print(has_two_numbers_sum(a, 19))
print(has_two_numbers_sum(a, 1))
print(has_two_numbers_sum(a, 6))

# Given an array, please determine whether it contains three numbers whose sum equals to 0.
def has_sum_zero(arr):
    for i in range(len(arr)):
        a = -arr[i]
        for j in arr[i+1:]:
            t = has_two_numers(arr[i+1:], j)
            if t:
                return a, t[0], t[1]


# Check if a substring is cointained within a given string
def strstr(needle, haystack):
    found = False
    for i in range(len(haystack)):
        aux = haystack[i:len(needle)]
        if aux == needle
            return True


