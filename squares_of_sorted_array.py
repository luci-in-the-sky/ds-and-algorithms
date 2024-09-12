# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

def squares_sorted(nums: list[int]) -> list[int]:
    non_negative_index =0
    for i in range(len(nums)):
        if nums[i] < 0:
            non_negative_index += 1
            #  N
    if non_negative_index == 0:
        return [num**2 for num in nums]
    else :
        new_nums = nums[non_negative_index:]
        negative_nums = nums[0:non_negative_index]
        for negative in negative_nums:
            # for every negative
            new_position = 0
            temp = - negative
            for j in range(len(new_nums)):
                if temp > new_nums[j]:
                    new_position += 1
            new_nums.insert(new_position, temp)
        return [new_num**2 for new_num in new_nums]




