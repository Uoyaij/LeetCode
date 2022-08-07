'''
# @Time : 2022/8/7 12:37
# @Author : Admin
# @Project : PythonCode
'''


# 先遍历物品，再遍历背包
def test_complete_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0] * (bag_weight + 1)  # 背包体积为j时所装的最大价值

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bag_weight])


# 先遍历背包，再遍历物品
def test_complete_pack2():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0] * (bag_weight + 1)

    for j in range(bag_weight + 1):
        for i in range(len(weight)):
            if j >= weight[i]:      # 如果背包体积大于物品体积
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bag_weight])


if __name__ == '__main__':
    test_complete_pack1()
    test_complete_pack2()
