import random

r = random.randint(1, 100)
while True:
    ans = int(input('請在1~100內猜數字: '))
    if ans == r:
        print('終於猜對了!')
        break
    elif r > ans:
        print('比答案小')
    else:
        print('比答案大')