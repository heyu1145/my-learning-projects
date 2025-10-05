try:
    dou_Input = float(input("Please input a number: "))
except ValueError:  # 修复：ValueError 不是 ValueException
    print("Please input a number!")
    exit()

Input = int(dou_Input)
if dou_Input != Input:
    print("Please input a Integer!")
    exit()

if Input < 0 or Input > 99999:
    print("The number is too small or too large!")
    exit()

str_Input = str(Input)
print(f"The number has {len(str_Input)} digits!")  # 修复：更通顺的表述

char_list = list(str_Input)

# 修复：使用 enumerate() 获取索引
for i, char in enumerate(char_list, 1):  # 从1开始计数
    print(f"Char {i}: {char}")

reverse = str_Input[::-1]
print(f"The number after reverse: {reverse}")
