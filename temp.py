def searchRange(nums, target):
    first = -1
    last = -1

    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            first = mid
            right= mid-1

        if nums[mid] < target:
            left = mid+1

        if nums[mid] > target:
            right = mid - 1

    left = 0
    right = len(nums)-1
        
    while left <= right:

        mid = (left +right) // 2

        if nums[mid] == target:
            last = mid
            left = mid+1

        if nums[mid] < target:
            left = mid+1

        if nums[mid] > target:
            right = mid - 1
    
    if left >= 0 and right < 0:
        right = left

    if right >=0 and left < 0:
        left = right

    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
target = 5

print(searchRange(nums,target))