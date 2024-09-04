# given a sorted array
def two_sum_sorted(nums: list[int], target: int) -> bool:
    head = 0
    tail = len(nums) - 1
    # while tail > 0 and head < len(nums):
    # better
    while head < tail :
        if nums[head] + nums[tail] > target:
            tail -= 1
        elif nums[head] + nums[tail] < target:
            head += 1
        elif nums[head] + nums[tail] == target:
            return True

    return False


if __name__ == "__main__":
    print(two_sum_sorted([1, 2, 4, 6, 8, 9, 14, 15], 13))

