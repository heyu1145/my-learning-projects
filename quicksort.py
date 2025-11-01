def quicksort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
