def find_second_largest(nums):
    if len(nums) < 2:
        return "List must have at least two elements"
    
    
    largest = second_largest = nums[0]
    
    for num in nums[1:]:
        if num > largest:
            # Update second largest and largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest if it's greater than current second largest
            second_largest = num
    
    if largest == second_largest:
        return "No second largest element found"
    
    return second_largest

# Test the function
nums = [10, 20, 4, 45, 99]
print("Second Largest Number :", find_second_largest(nums))
