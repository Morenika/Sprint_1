def digit_root(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num


# Примеры
print(digit_root(4851))     # 9
print(digit_root(97569))    # 9
print(digit_root(889987))   # 4
