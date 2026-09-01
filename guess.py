# -*- coding: utf-8 -*-
# 猜数字游戏：电脑随机想一个 1~100 的数，你来猜，猜对为止。
# 运行方法：在终端输入 python3 guess.py 然后回车

import random  # 导入"随机"模块，后面用它生成随机数

# 游戏开始提示
print("=" * 30)
print("欢迎来玩猜数字游戏！")
print("我心里想了一个 1~100 之间的数字")
print("=" * 30)

# 生成 1~100 之间的随机数，存到变量 answer 里
answer = random.randint(1, 100)

# guesses 记录你猜了几次，从 0 开始
guesses = 0

# 无限循环：只要没猜对就一直猜
while True:
    # 让玩家输入一个数字（input 返回的是文字，int 把它变成数字）
    guess_text = input("请输入你的猜测：")

    # 如果输入的不是数字会报错，用 try/except 兜住
    try:
        guess = int(guess_text)
    except ValueError:
        print("请输入数字哦！")
        continue  # continue = 跳过下面所有代码，回到循环开头

    # 每猜一次，次数加 1
    guesses = guesses + 1

    # 判断：大了？小了？还是猜中了？
    if guess > answer:
        print("太大了，再往小猜猜！")
    elif guess < answer:
        print("太小了，再往大猜猜！")
    else:
        # 猜中了！
        print("=" * 30)
        print(f"恭喜你猜对了！答案就是 {answer}，你一共猜了 {guesses} 次。")
        # 根据次数给不同评语
        if guesses <= 5:
            print("天才级别！")
        elif guesses <= 10:
            print("很厉害！")
        else:
            print("还不错，下次可以更快！")
        print("=" * 30)
        break  # break = 退出循环，游戏结束
