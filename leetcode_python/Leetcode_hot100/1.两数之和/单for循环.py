'''
# @Time : 2022/7/13 10:23
# @Author : Admin
# @Project : PythonCode
'''


def twoSum(nums, target):
    n = len(nums)
    for x in range(n):
        a = target - nums[x]
        if a in nums:  # 判断a有没有在nums数组里
            y = nums.index(a)  # 有的话，那么用index获取到该数字的下标
            print("y", y)
            if x == y:
                continue  # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
            else:  # 否则就返回结果
                return x, y
        else:
            continue  # 上面的条件都不满足就跳过，进行下一次循环


nums = [1, 2, 1, 2]
target = 3
print(twoSum(nums, target))
