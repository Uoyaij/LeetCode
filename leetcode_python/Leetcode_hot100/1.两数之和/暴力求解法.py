'''
# @Time : 2022/7/12 17:42
# @Author : Admin
# @Project : PythonCode
'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    print("nums", len(nums))
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # 找到结果，跳出循环
                return i, j
                break
            else:
                continue


nums = [1, 2, 3, 4]
target = 4
print(twoSum(nums, target))
