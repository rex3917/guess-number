import random

r = random.randint(1, 100)
count = 0
while True:
    ans = int(input('請在1~100內猜數字: '))
    count += 1
    if ans == r:
        print('終於猜對了!')
        print('總共猜了', count, '次')
        break
    elif r > ans:
        print('比答案小')
    else:
        print('比答案大')