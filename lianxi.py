input_1 = input("输入:")
while True:
    try:
        input_num = int(input_1)
        if 0 < input_num < 12:
            print("666")
        break
    except (RuntimeError, TypeError, NameError,ValueError):
        input_1 = input("再次输入:")
