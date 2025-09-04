import random

# 1. 让程序生成一个 1 到 100 之间的随机数
secret_number = random.randint(1, 100)

# 初始化一个变量，用于存储用户的猜测，随便给个值，只要不是正确答案就行
guess = 0

print("欢迎来到猜数字游戏！")
print("我已经想好了一个 1 到 100 之间的数字，你来猜猜看吧！")

# 2. 使用循环，直到用户猜对
while guess != secret_number:
    try:
        # 3. 获取用户的输入，并转换为整数
        guess = int(input("请输入你的猜测："))

        # 4. 比较猜测和正确答案
        if guess < secret_number:
            print("你猜得太小了，再试一次！")
        elif guess > secret_number:
            print("你猜得太大了，再试一次！")
        else:
            print("恭喜你，猜对了！")
            # 当猜对时，循环自动结束
    except ValueError:
        # 处理非数字输入的情况
        print("这不是一个有效的数字，请重新输入。")
        
print("游戏结束！")