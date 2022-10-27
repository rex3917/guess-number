import random

a = int(input('請決定隨機數字範圍開始值: '))
b = int(input('請決定隨機數字範圍結束值: '))
r = random.randint(a, b)
count = 0
while True:
    ans = int(input('請在1~100內猜數字: '))
    if ans > b or ans < a:
        print('數字超出範圍')
    count += 1
    if ans == r:
        print('終於猜對了!')
        print('總共猜了', count, '次')
        break
    elif r > ans:
        print('比答案小')
    else:
        print('比答案大')