# Написать функцию make_exchange(money, coins), которая принимает сумму денег (целое число) и массив номиналов
# разменных монет (целых чисел) (возможно пустой) и возвращает количество способов произвести размен.
# Считаем, что разменных монет бесконечное множество.
# Ввод: 10, [5,2,3] Вывод: 4
def make_exchange(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for higher_amount in range(coin, money + 1):
            higher_amount_remainder = higher_amount - coin
            dp[higher_amount] += dp[higher_amount_remainder]
    #print(*dp)
    return dp[money]


money = 10
coins = [5 ,2 ,3]
print(make_exchange(money, coins))
