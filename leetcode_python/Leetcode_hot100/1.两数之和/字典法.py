'''
# @Time : 2022/7/12 18:11
# @Author : Admin
# @Project : PythonCode
--------------------------------------------
本题思路：
字典法。
字典：dic = {key1 : value1, key2 : value2 }
1。首先遍历nums列表，目标值-遍历值不在字典中，记录该值和值的索引
2。发现目标值-遍历值在字典中，说明前面已经出现过，返回前一个值的索引和当前值的索引
'''


def twoSum(nums, target):
    d = {}
    n = len(nums)
    for x in range(n):
        print("res", target - nums[x])
        if target - nums[x] in d:  # 看另外一个数字有没有在字典里
            return d[target - nums[x]], x  # 有的话直接就可以返回value了;没有的话会继续循环
        else:
            d[nums[x]] = x
        print("d", d)


nums = [2, 3, 5, 6, 7, 9, 77]
target = 86
print(twoSum(nums, target))


