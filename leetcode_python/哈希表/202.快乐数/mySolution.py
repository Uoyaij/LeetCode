'''
# @Time : 2022/7/28 10:21
# @Author : Admin
# @Project : PythonCode
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum_ = 0
            # 从个位开始依次取，平方求和
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        set1 = set()
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            if n in set1:
                return False
            else:
                set1.add(n)

    # 快慢指针
    def isHappy2(self, n: int) -> bool:
        """
        如果n是一个快乐数，即没有循环，那么快跑者最终会比慢跑者先到达数字1
        如果n不是一个快乐的数字，那么最终快跑者和慢跑者将在同一个数字1相遇
        :param self:
        :param n:
        :return:
        """
        def get_next(number):
            sum1 = 0
            while number:
                sum1 += (number % 10) ** 2
                number //= 10
            return sum1

        slow_runner = n
        fast_runner = get_next(n)
        while True:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
            if fast_runner == 1:
                return True
            if slow_runner == fast_runner:
                return False


n = 19
solution = Solution()
print(solution.isHappy2(n))
