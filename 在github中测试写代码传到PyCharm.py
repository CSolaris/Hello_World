import datetime

# 获取当前日期和时间
current_time = datetime.datetime.now()

# 打印当前日期和时间
print(f"当前日期和时间: {current_time}")

# 定义一个计算平方的函数
def calculate_square(number):
    return number ** 2

# 给定数字
number = 7

# 计算并打印数字的平方
square = calculate_square(number)
print(f"{number} 的平方是: {square}")
