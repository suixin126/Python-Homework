# 让用户输入一个非零整数
try:
    num = int(input("请输入一个非零整数: "))
    if num == 0:
        raise ValueError("输入的数不能为零")

        # 计算并打印该整数的倒数
    reciprocal = 1 / num
    print("整数的倒数是:", reciprocal)

    # 计算并打印该整数的平方和立方
    square = num ** 2
    cube = num ** 3
    print("整数的平方是:", square)
    print("整数的立方是:", cube)

except ValueError as e:
    print("错误:", str(e))
except ZeroDivisionError as e:
    print("错误: 不能除以零")