def decimal_to_binary():
    x = int(input("请输入一个十进制整数: "))  # 输入十进制整数
    w = 1  # 初始化权值，控制二进制位的权重
    s = 0  # 存储转换后的二进制数

    while x > 0:
        r = x % 2  # 取余数，得到当前位的二进制值
        s = s + r * w  # 累加二进制结果
        w = w * 10 # 权值倍增，进入下一个二进制位
        x = x // 2  # 商更新，进行下一轮取余

    print("对应的二进制是:", s)

# 测试
decimal_to_binary()
