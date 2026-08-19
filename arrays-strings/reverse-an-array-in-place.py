def reverse_array(nums):
    ptr_1 = 0
    ptr_2 = len(nums) - 1
    
    while ptr_1 < ptr_2:
        front = nums[ptr_1]
        back = nums[ptr_2]

        nums[ptr_1] = back
        nums[ptr_2] = front

        ptr_1 +=1
        ptr_2 -=1
    
    return nums
 