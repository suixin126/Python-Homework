import math

# 让用户输入三个整数，分别代表角度
try:
    angle1 = int(input("请输入第一个角度: "))
    angle2 = int(input("请输入第二个角度: "))
    angle3 = int(input("请输入第三个角度: "))

    # 计算并打印这些角度的正弦、余弦和正切值
    sin1 = math.sin(math.radians(angle1))
    cos1 = math.cos(math.radians(angle1))
    tan1 = math.tan(math.radians(angle1))
    sin2 = math.sin(math.radians(angle2))
    cos2 = math.cos(math.radians(angle2))
    tan2 = math.tan(math.radians(angle2))
    sin3 = math.sin(math.radians(angle3))
    cos3 = math.cos(math.radians(angle3))
    tan3 = math.tan(math.radians(angle3))

    # 对每个角度的正弦值进行四舍五入到两位小数
    sin1_rounded = round(sin1, 2)
    sin2_rounded = round(sin2, 2)
    sin3_rounded = round(sin3, 2)

    # 计算这三个角度的正弦值的总和，并使用取余运算得到与10的余数
    sin_sum = sin1 + sin2 + sin3
    remainder = sin_sum % 10

    # 计算并打印正弦总和的整数部分
    sin_sum_integer_part = int(sin_sum)

    print(f"角度 {angle1} 的正弦、余弦和正切值分别是: {sin1_rounded}, {cos1:.2f}, {tan1:.2f}")
    print(f"角度 {angle2} 的正弦、余弦和正切值分别是: {sin2_rounded}, {cos2:.2f}, {tan2:.2f}")
    print(f"角度 {angle3} 的正弦、余弦和正切值分别是: {sin3_rounded}, {cos3:.2f}, {tan3:.2f}")
    print("正弦值的总和与10的余数是:", remainder)
    print("正弦总和的整数部分是:", sin_sum_integer_part)

except ValueError as e:
    print("错误: 输入必须为整数")
except Exception as e:
    print("发生了一个错误:", str(e))