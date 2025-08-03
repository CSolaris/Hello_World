import random

# 生成一个 1 到 100 的随机整数
secret_number = random.randint(1, 100)

print("欢迎来到猜数字游戏！我已经选好了 1 到 100 之间的一个数字。")

while True:
    guess = input("请输入你猜的数字：")

    # 检查输入是否合法
    if not guess.isdigit():
        print("请输入一个有效的整数！")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("你猜的太小了，再试一次吧！")
    elif guess > secret_number:
        print("你猜的太大了，再试一次吧！")
    else:
        print(f"恭喜你，猜对了！正确答案是 {secret_number}")
        break
