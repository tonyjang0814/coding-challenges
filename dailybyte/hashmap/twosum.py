def twoSum(nums,target):
    contents = dict()
    for i in nums:
        contents[i] = 1
    
    for i in nums:
        value_to_look = target-i
        if value_to_look in contents:
            return True
    return False