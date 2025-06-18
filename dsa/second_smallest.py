nums = [4, 2, 1, 3, 5]

# Function to find the second smallest number in a list
def second_smallest(nums):
    smallest = second_smallest = nums[0]
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None

result = second_smallest(nums)
print(f"The second smallest number in {nums} is {result}.")

# function to find 2nd largest number in a list
def second_largest(nums):
    largest = second_largest = nums[0]
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None

result_largest = second_largest(nums)
print(f"The second largest number in {nums} is {result_largest}.")

